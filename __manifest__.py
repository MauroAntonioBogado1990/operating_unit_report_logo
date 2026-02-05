{
    "name": "Operating Unit Report Logo",
    "version": "13.0.1.0.0",
    "summary": "Use an operating unit specific logo in reports (fallback to company logo)",
    "category": "Localization/Accounting",
    "author": "Custom",
    "website": "",
    "license": "AGPL-3",
    "depends": [
        "operating_unit",
        "account",
        "web"
    ],
    "data": [
        "views/report_external_logo.xml",
        "views/operating_unit_views.xml"
    ],
    "installable": True,
    "auto_install": False,
}
