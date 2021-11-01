/*
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include <string>
#include "globalization_js.hpp"
#include "globalization_ndk.hpp"

using namespace std;

/**
 * Default constructor.
 */
GlobalizationJS::GlobalizationJS(const std::string& id) :
		m_id(id) {
	m_pGlobalizationController = new webworks::GlobalizationNDK(this);
}

/**
 * GlobalizationJS destructor.
 */
GlobalizationJS::~GlobalizationJS() {
	if (m_pGlobalizationController)
		delete m_pGlobalizationController;
}

/**
 * This method returns the list of objects implemented by this native
 * extension.
 */
char* onGetObjList() {
	static char name[] = "Globalization";
	return name;
}

/**
 * This method is used by JNext to instantiate the GlobalizationJS object when
 * an object is created on the JavaScript server side.
 */
JSExt* onCreateObject(const string& className, const string& id) {
	if (className == "Globalization") {
		return new GlobalizationJS(id);
	}

	return NULL;
}

/**
 * Method used by JNext to determine if the object can be deleted.
 */
bool GlobalizationJS::CanDelete() {
	return true;
}

/**
 * It will be called from JNext JavaScript side with passed string.
 * This method implements the interface for the JavaScript to native binding
 * for invoking native code. This method is triggered when JNext.invoke is
 * called on the JavaScript side with this native objects id.
 */
string GlobalizationJS::InvokeMethod(const string& command) {
	// format must be: "command callbackId params"
	size_t commandIndex = command.find_first_of(" ");
	std::string strCommand = command.substr(0, commandIndex);
	size_t callbackIndex = command.find_first_of(" ", commandIndex + 1);
	std::string callbackId = command.substr(commandIndex + 1, callbackIndex - commandIndex - 1);
	std::string arg = command.substr(callbackIndex + 1, command.length());

	// based on the command given, run the appropriate method in globalizationndk.cpp
    if (strCommand == "getPreferredLanguage") {
        return m_pGlobalizationController->getPreferredLanguage();
    } else if (strCommand == "getLocaleName") {
        return m_pGlobalizationController->getLocaleName();
    } else if (strCommand == "dateToString") {
        return m_pGlobalizationController->dateToString(arg);
    } else if (strCommand == "stringToDate") {
        return m_pGlobalizationController->stringToDate(arg);
    } else if (strCommand == "getDatePattern") {
        return m_pGlobalizationController->getDatePattern(arg);
    } else if (strCommand == "getDateNames") {
        return m_pGlobalizationController->getDateNames(arg);
    } else if (strCommand == "isDayLightSavingsTime") {
        return m_pGlobalizationController->isDayLightSavingsTime(arg);
    } else if (strCommand == "getFirstDayOfWeek") {
        return m_pGlobalizationController->getFirstDayOfWeek();
    } else if (strCommand == "numberToString") {
        return m_pGlobalizationController->numberToString(arg);
    } else if (strCommand == "stringToNumber") {
        return m_pGlobalizationController->stringToNumber(arg);
    } else if (strCommand == "getNumberPattern") {
        return m_pGlobalizationController->getNumberPattern(arg);
    } else if (strCommand == "getCurrencyPattern") {
        return m_pGlobalizationController->getCurrencyPattern(arg);
	}

	strCommand.append(";");
	strCommand.append(command);
	return strCommand;
}

// Notifies JavaScript of an event
void GlobalizationJS::NotifyEvent(const std::string& event) {
	std::string eventString = m_id + " ";
	eventString.append(event);
	SendPluginEvent(eventString.c_str(), m_pContext);
}
