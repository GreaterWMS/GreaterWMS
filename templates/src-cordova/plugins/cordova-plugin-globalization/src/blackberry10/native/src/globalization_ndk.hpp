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

#ifndef GLOBALIZATIONNDK_HPP_
#define GLOBALIZATIONNDK_HPP_

#include <string>

class GlobalizationJS;

namespace webworks {

class GlobalizationNDK {
public:
	explicit GlobalizationNDK(GlobalizationJS *parent = NULL);
	virtual ~GlobalizationNDK();

	// The extension methods are defined here

    std::string getPreferredLanguage();

    std::string getLocaleName();

    std::string dateToString(const std::string& args);

    std::string stringToDate(const std::string& args);

    std::string getDatePattern(const std::string& args);

    std::string getDateNames(const std::string& args);

    std::string isDayLightSavingsTime(const std::string& args);

    std::string getFirstDayOfWeek();

    std::string numberToString(const std::string& args);

    std::string stringToNumber(const std::string& args);

    std::string getNumberPattern(const std::string& args);

    std::string getCurrencyPattern(const std::string& args);

private:
	GlobalizationJS *m_pParent;
};

} // namespace webworks

#endif /* GLOBALIZATIONNDK_H_ */
