import mock
import StringIO
import wifiphisher.common.constants as constant
import wifiphisher.common.macmatcher as macmatcher


@mock.patch("__builtin__.open")
def test_parse_oui_file(mock_open):
    """
    Test parse_oui_file function with a single entry file
    """
    oui_file = "FILE LOCATION"
    identifier = "07db21"
    vendor = "HELL"
    logo = ""

    mock_open.return_value = StringIO.StringIO("{}|{}|{}".format(identifier, vendor, logo))
    actual = macmatcher.parse_oui_file(oui_file)
    expected = {identifier: (vendor, logo)}
    message = "Failed to parse the oui file"

    assert actual == expected, message


def test_mac_to_oui_all_lower_case():
    """
    Test mac_to_oui function with all lower case input
    """

    mac_address = "a3:44:6d:25:cc:0b"

    actual = macmatcher.mac_to_oui(mac_address)
    expected = "A3446D"

    assert actual == expected


def test_mac_to_oui_all_uppper_case():
    """
    Test mac_to_oui function with all upper case input
    """

    mac_address = "A3:44:6D:25:CC:0B"

    actual = macmatcher.mac_to_oui(mac_address)
    expected = "A3446D"

    assert actual == expected

