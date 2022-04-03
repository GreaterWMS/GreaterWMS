using System;
using System.Reflection;
using System.Xml.Linq;
using Windows.ApplicationModel;
using WPCordovaClassLib.Cordova;
using WPCordovaClassLib.Cordova.Commands;

namespace Cordova.Extension.Commands
{
	public class AppVersion : BaseCommand
	{
		public void getVersionNumber(string empty)
		{
			string version;
			if (Environment.OSVersion.Version.Major <= 8)
			{
				// Package.Current.Id is NOT working in Windows Phone 8
				// Workaround based on http://stackoverflow.com/questions/14371275/how-can-i-get-my-windows-store-apps-title-and-version-info
				version = XDocument.Load("WMAppManifest.xml").Root.Element("App").Attribute("Version").Value;
			}
			else
			{
				version = Package.Current.Id.Version.ToString();
			}

			this.DispatchCommandResult(new PluginResult(PluginResult.Status.OK, version));
		}

		public void getAppName(string empty)
		{
			string name;
			if (Environment.OSVersion.Version.Major <= 8)
			{
				//Windows.ApplicationModel.Package.Current.Id is NOT working in Windows Phone 8
				//Workaround based on http://stackoverflow.com/questions/14371275/how-can-i-get-my-windows-store-apps-title-and-version-info
				name = XDocument.Load("WMAppManifest.xml").Root.Element("App").Attribute("Title").Value;
			}
			else
			{
				name = Package.Current.Id.Name;
			}

			this.DispatchCommandResult(new PluginResult(PluginResult.Status.OK, name));
		}

		public void getPackageName(string empty)
		{
			string package = Assembly.GetExecutingAssembly().GetName().Name;

			this.DispatchCommandResult(new PluginResult(PluginResult.Status.OK, package));
		}
	}
}