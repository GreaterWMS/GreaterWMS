/*
       Licensed to the Apache Software Foundation (ASF) under one
       or more contributor license agreements.  See the NOTICE file
       distributed with this work for additional information
       regarding copyright ownership.  The ASF licenses this file
       to you under the Apache License, Version 2.0 (the
       "License"); you may not use this file except in compliance
       with the License.  You may obtain a copy of the License at

         http://www.apache.org/licenses/LICENSE-2.0

       Unless required by applicable law or agreed to in writing,
       software distributed under the License is distributed on an
       "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
       KIND, either express or implied.  See the License for the
       specific language governing permissions and limitations
       under the License.
*/

package org.apache.cordova.globalization;

import org.json.JSONException;
import org.json.JSONObject;

/** 
 * @description Exception class representing defined Globalization error codes
 * @Globalization error codes:
 *      GlobalizationError.UNKNOWN_ERROR = 0;
 *      GlobalizationError.FORMATTING_ERROR = 1;   
 *      GlobalizationError.PARSING_ERROR = 2;   
 *      GlobalizationError.PATTERN_ERROR = 3;
 */
public class GlobalizationError extends Exception{
    /**
     * 
     */
    private static final long serialVersionUID = 1L;
    public static final String UNKNOWN_ERROR = "UNKNOWN_ERROR";
    public static final String FORMATTING_ERROR = "FORMATTING_ERROR";
    public static final String PARSING_ERROR = "PARSING_ERROR";
    public static final String PATTERN_ERROR = "PATTERN_ERROR";
    
    int error = 0;  //default unknown error thrown
    /**
     * Default constructor        
     */
    public GlobalizationError() {}
    /**
     * Create an exception returning an error code 
     *    
     * @param   s           
     */
    public GlobalizationError(String s) {       
        if (s.equalsIgnoreCase(FORMATTING_ERROR)){
            error = 1;
        }else if (s.equalsIgnoreCase(PARSING_ERROR)){
            error = 2;
        }else if (s.equalsIgnoreCase(PATTERN_ERROR)){
            error = 3;
        }       
    }
    /**
     * get error string based on error code 
     *    
     * @param   String msg           
     */
    public String getErrorString(){
        String msg = "";
        switch (error){
        case 0:
            msg = UNKNOWN_ERROR;
            break;
        case 1:
            msg =  FORMATTING_ERROR;
            break;
        case 2:
            msg =  PARSING_ERROR;
            break;
        case 3:
            msg =  PATTERN_ERROR;
            break;
        }
        return msg;
    }
    /**
     * get error code 
     *    
     * @param   String msg           
     */
    public int getErrorCode(){      
        return error;
    }
    
    /**
     * get the json version of this object to return to javascript
     * @return
     */
    public JSONObject toJson() {
        JSONObject obj = new JSONObject();
        try {
            obj.put("code", getErrorCode());
            obj.put("message", getErrorString());
        } catch (JSONException e) {
            // never happens
        }
        return obj;
    }
}
