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

#ifndef GlobalizationJS_HPP_
#define GlobalizationJS_HPP_

#include <string>
#include "../public/plugin.h"
#include "globalization_ndk.hpp"

class GlobalizationJS: public JSExt {

public:
    explicit GlobalizationJS(const std::string& id);
    virtual ~GlobalizationJS();
    virtual bool CanDelete();
    virtual std::string InvokeMethod(const std::string& command);
    void NotifyEvent(const std::string& event);

private:
    std::string m_id;
    // Definition of a pointer to the actual native extension code
    webworks::GlobalizationNDK *m_pGlobalizationController;
};

#endif /* GlobalizationJS_HPP_ */
