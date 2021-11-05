// (c) 2104 Don Coleman
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package com.megster.cordova.ble.central;

import java.util.UUID;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class UUIDHelper {

    // base UUID used to build 128 bit Bluetooth UUIDs
    public static final String UUID_BASE = "0000XXXX-0000-1000-8000-00805f9b34fb";
    // reuse pattern
    private static final Pattern pattern = Pattern.compile("0000(.{4})-0000-1000-8000-00805f9b34fb", Pattern.CASE_INSENSITIVE);

    // handle 16 and 128 bit UUIDs
    public static UUID uuidFromString(String uuid) {

        if (uuid.length() == 4) {
            uuid = UUID_BASE.replace("XXXX", uuid);
        }
        return UUID.fromString(uuid);
    }

    // return 16 bit UUIDs where possible
    public static String uuidToString(UUID uuid) {
        String longUUID = uuid.toString();
        Matcher matcher = pattern.matcher(longUUID);
        if (matcher.matches()) {
            // 16 bit UUID
            return matcher.group(1);
        } else {
            return longUUID;
        }
    }
}
