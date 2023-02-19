def set_wu_settings(level=None,
                    recommended=None,
                    featured=None,
                    elevated=None,
                    msupdate=None,
                    day=None,
                    time=None):
    '''
    Change Windows Update settings. If no parameters are passed, the current
    value will be returned.

    Supported:
        - Windows Vista / Server 2008
        - Windows 7 / Server 2008R2
        - Windows 8 / Server 2012
        - Windows 8.1 / Server 2012R2

    .. note:
        Microsoft began using the Unified Update Platform (UUP) starting with
        Windows 10 / Server 2016. The Windows Update settings have changed and
        the ability to 'Save' Windows Update settings has been removed. Windows
        Update settings are read-only. See MSDN documentation:
        https://msdn.microsoft.com/en-us/library/aa385829(v=vs.85).aspx

    Args:

        level (int):
            Number from 1 to 4 indicating the update level:

            1. Never check for updates
            2. Check for updates but let me choose whether to download and install them
            3. Download updates but let me choose whether to install them
            4. Install updates automatically

        recommended (bool):
            Boolean value that indicates whether to include optional or
            recommended updates when a search for updates and installation of
            updates is performed.

        featured (bool):
            Boolean value that indicates whether to display notifications for
            featured updates.

        elevated (bool):
            Boolean value that indicates whether non-administrators can perform
            some update-related actions without administrator approval.

        msupdate (bool):
            Boolean value that indicates whether to turn on Microsoft Update for
            other Microsoft products

        day (str):
            Days of the week on which Automatic Updates installs or uninstalls
            updates. Accepted values:

            - Everyday
            - Monday
            - Tuesday
            - Wednesday
            - Thursday
            - Friday
            - Saturday

        time (str):
            Time at which Automatic Updates installs or uninstalls updates. Must
            be in the ##:## 24hr format, eg. 3:00 PM would be 15:00. Must be in
            1 hour increments.

    Returns:

        dict: Returns a dictionary containing the results.

    CLI Examples:

    .. code-block:: bash

        salt '*' win_wua.set_wu_settings level=4 recommended=True featured=False
    '''
    # The AutomaticUpdateSettings.Save() method used in this function does not
    # work on Windows 10 / Server 2016. It is called in throughout this function
    # like this:
    #
    # with salt.utils.winapi.Com():
    #     obj_au = win32com.client.Dispatch('Microsoft.Update.AutoUpdate')
    #     obj_au_settings = obj_au.Settings
    #     obj_au_settings.Save()
    #
    # The `Save()` method reports success but doesn't actually change anything.
    # Windows Update settings are read-only in Windows 10 / Server 2016. There's
    # a little blurb on MSDN that mentions this, but gives no alternative for
    # changing these settings in Windows 10 / Server 2016.
    #
    # https://msdn.microsoft.com/en-us/library/aa385829(v=vs.85).aspx
    #
    # Apparently the Windows Update framework in Windows Vista - Windows 8.1 has
    # been changed quite a bit in Windows 10 / Server 2016. It is now called the
    # Unified Update Platform (UUP). I haven't found an API or a Powershell
    # commandlet for working with the the UUP. Perhaps there will be something
    # forthcoming. The `win_lgpo` module might be an option for changing the
    # Windows Update settings using local group policy.
    ret = {'Success': True}

    # Initialize the PyCom system
    with salt.utils.winapi.Com():

        # Create an AutoUpdate object
        obj_au = win32com.client.Dispatch('Microsoft.Update.AutoUpdate')

    # Create an AutoUpdate Settings Object
    obj_au_settings = obj_au.Settings

    # Only change the setting if it's passed
    if level is not None:
        obj_au_settings.NotificationLevel = int(level)
        result = obj_au_settings.Save()
        if result is None:
            ret['Level'] = level
        else:
            ret['Comment'] = "Settings failed to save. Check permissions."
            ret['Success'] = False

    if recommended is not None:
        obj_au_settings.IncludeRecommendedUpdates = recommended
        result = obj_au_settings.Save()
        if result is None:
            ret['Recommended'] = recommended
        else:
            ret['Comment'] = "Settings failed to save. Check permissions."
            ret['Success'] = False

    if featured is not None:
        obj_au_settings.FeaturedUpdatesEnabled = featured
        result = obj_au_settings.Save()
        if result is None:
            ret['Featured'] = featured
        else:
            ret['Comment'] = "Settings failed to save. Check permissions."
            ret['Success'] = False

    if elevated is not None:
        obj_au_settings.NonAdministratorsElevated = elevated
        result = obj_au_settings.Save()
        if result is None:
            ret['Elevated'] = elevated
        else:
            ret['Comment'] = "Settings failed to save. Check permissions."
            ret['Success'] = False

    if day is not None:
        # Check that day is valid
        days = {'Everyday': 0,
                'Sunday': 1,
                'Monday': 2,
                'Tuesday': 3,
                'Wednesday': 4,
                'Thursday': 5,
                'Friday': 6,
                'Saturday': 7}
        if day not in days:
            ret['Comment'] = "Day needs to be one of the following: Everyday," \
                             "Monday, Tuesday, Wednesday, Thursday, Friday, " \
                             "Saturday"
            ret['Success'] = False
        else:
            # Set the numeric equivalent for the day setting
            obj_au_settings.ScheduledInstallationDay = days[day]
            result = obj_au_settings.Save()
            if result is None:
                ret['Day'] = day
            else:
                ret['Comment'] = "Settings failed to save. Check permissions."
                ret['Success'] = False

    if time is not None:
        # Check for time as a string: if the time is not quoted, yaml will
        # treat it as an integer
        if not isinstance(time, six.string_types):
            ret['Comment'] = "Time argument needs to be a string; it may need to"\
                             "be quoted. Passed {0}. Time not set.".format(time)
            ret['Success'] = False
        # Check for colon in the time
        elif ':' not in time:
            ret['Comment'] = "Time argument needs to be in 00:00 format." \
                             " Passed {0}. Time not set.".format(time)
            ret['Success'] = False
        else:
            # Split the time by :
            t = time.split(":")
            # We only need the hours value
            obj_au_settings.FeaturedUpdatesEnabled = t[0]
            result = obj_au_settings.Save()
            if result is None:
                ret['Time'] = time
            else:
                ret['Comment'] = "Settings failed to save. Check permissions."
                ret['Success'] = False

    if msupdate is not None:
        # Microsoft Update requires special handling
        # First load the MS Update Service Manager
        with salt.utils.winapi.Com():
            obj_sm = win32com.client.Dispatch('Microsoft.Update.ServiceManager')

        # Give it a bogus name
        obj_sm.ClientApplicationID = "My App"

        if msupdate:
            # msupdate is true, so add it to the services
            try:
                obj_sm.AddService2('7971f918-a847-4430-9279-4a52d1efe18d', 7, '')
                ret['msupdate'] = msupdate
            except Exception as error:
                hr, msg, exc, arg = error.args  # pylint: disable=W0633
                # Consider checking for -2147024891 (0x80070005) Access Denied
                ret['Comment'] = "Failed with failure code: {0}".format(exc[5])
                ret['Success'] = False
        else:
            # msupdate is false, so remove it from the services
            # check to see if the update is there or the RemoveService function
            # will fail
            if _get_msupdate_status():
                # Service found, remove the service
                try:
                    obj_sm.RemoveService('7971f918-a847-4430-9279-4a52d1efe18d')
                    ret['msupdate'] = msupdate
                except Exception as error:
                    hr, msg, exc, arg = error.args  # pylint: disable=W0633
                    # Consider checking for the following
                    # -2147024891 (0x80070005) Access Denied
                    # -2145091564 (0x80248014) Service Not Found (shouldn't get
                    # this with the check for _get_msupdate_status above
                    ret['Comment'] = "Failed with failure code: {0}".format(exc[5])
                    ret['Success'] = False
            else:
                ret['msupdate'] = msupdate

    ret['Reboot'] = get_needs_reboot()

    return ret