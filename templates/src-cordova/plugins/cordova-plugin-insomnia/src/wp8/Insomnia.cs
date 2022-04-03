using Microsoft.Phone.Shell;

namespace WPCordovaClassLib.Cordova.Commands
{
    public class Insomnia : BaseCommand
    {
        public void keepAwake(string options) 
        {
            PhoneApplicationService.Current.UserIdleDetectionMode = IdleDetectionMode.Disabled;
            DispatchCommandResult(new PluginResult(PluginResult.Status.OK));
        }

        public void allowSleepAgain(string options) 
        {
            PhoneApplicationService.Current.UserIdleDetectionMode = IdleDetectionMode.Enabled;
            DispatchCommandResult(new PluginResult(PluginResult.Status.OK));
        }
    }
}
