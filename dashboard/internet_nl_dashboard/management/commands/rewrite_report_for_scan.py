import logging

from django.core.management.base import BaseCommand

from dashboard.internet_nl_dashboard.logic.urllist_dashboard_report import create_dashboard_report_at
from dashboard.internet_nl_dashboard.models import AccountInternetNLScan
from dashboard.internet_nl_dashboard.scanners.scan_internet_nl_per_account import (
    upgrade_report_with_statistics, upgrade_report_with_unscannable_urls,
    connect_urllistreport_to_accountinternetnlscan)

log = logging.getLogger(__package__)


class Command(BaseCommand):
    help = 'Overwrite an existing report. This can be useful if the reporting logic has changed.'

    def add_arguments(self, parser):
        parser.add_argument('--scan', type=int, required=True)
        super().add_arguments(parser)

    def handle(self, *args, **options):

        # See if we can find the scan
        if not options['scan']:
            raise ValueError("No scan id given")

        scan = AccountInternetNLScan.objects.all().filter(scan=options['scan']).first()

        if not scan:
            raise ValueError("Scan does not exist")

        if not scan.report.at_when:
            raise ValueError("No report created yet, will not create a new report when the process is running.")

        old_report_moment = scan.report.at_when

        # remove the old report, we don't store duplicates:
        scan.report.delete()

        # create new report and associate it.
        urllistreport = create_dashboard_report_at(scan.urllist, old_report_moment)
        urllistreport = connect_urllistreport_to_accountinternetnlscan(urllistreport, scan)
        urllistreport = upgrade_report_with_statistics(urllistreport)
        upgrade_report_with_unscannable_urls(urllistreport, scan)

        log.debug("Done!")
