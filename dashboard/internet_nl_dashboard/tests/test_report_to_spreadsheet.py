from websecmap.reporting.report import create_timeline, create_url_report

from dashboard.internet_nl_dashboard.logic.domains import (_add_to_urls_to_urllist,
                                                           get_or_create_list_by_name)
from dashboard.internet_nl_dashboard.logic.report_to_spreadsheet import (create_spreadsheet,
                                                                         upgrade_excel_spreadsheet)
from dashboard.internet_nl_dashboard.models import UrlListReport
from dashboard.internet_nl_dashboard.tests import (create_scan_report,
                                                   make_url_with_endpoint_and_scan)


def test_report_to_spreadsheet(db) -> None:
    account, url, endpoint, scan = make_url_with_endpoint_and_scan()

    urllist = get_or_create_list_by_name(account, "test list 1")
    _add_to_urls_to_urllist(account, urllist, [url])
    create_url_report(create_timeline(url), url)
    create_scan_report(account, urllist)

    # make sure there is a urllistreport to get a spreadsheet from
    assert UrlListReport.objects.all().count() == 1

    filename, spreadsheet = create_spreadsheet(account=account, report_id=urllist.pk)

    # there should be a spreadsheet
    assert spreadsheet

    tmp_file_handle = upgrade_excel_spreadsheet(spreadsheet)

    # and there should be a file handle
    assert tmp_file_handle
