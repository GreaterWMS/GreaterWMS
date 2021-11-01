// Type definitions for cordova-plugin-battery-status
// Project: https://github.com/apache/cordova-plugin-battery-status
// Definitions by: Microsoft Open Technologies Inc <http://msopentech.com>
//                 Tim Brust <https://github.com/timbru31>
// Definitions: https://github.com/DefinitelyTyped/DefinitelyTyped

type batteryEvent = 'batterystatus' | 'batterycritical' | 'batterylow';

interface Window {
    onbatterystatus: (type: BatteryStatusEvent) => void;
    onbatterycritical: (type: BatteryStatusEvent) => void;
    onbatterylow: (type: BatteryStatusEvent) => void;
    /**
     * Adds a listener for an event from the BatteryStatus plugin.
     * @param type       - The event to listen for.
     * 
     *                     `batterystatus`: event fires when the percentage of battery charge changes by at least 1 percent, or if the device is plugged in or unplugged.
     * 
     *                     `batterycritical`: event fires when the percentage of battery charge has reached the critical battery threshold. The value is device-specific.
     * 
     *                     `batterylow`: event fires when the percentage of battery charge has reached the low battery threshold, device-specific value.
     * @param listener   - The function that executes when the event fires. The function is passed an BatteryStatusEvent object as a parameter.
     * @param useCapture - A Boolean indicating whether events of this type will be dispatched to the registered listener before being dispatched to any EventTarget beneath it in the DOM tree.
     */
    addEventListener(type: batteryEvent, listener: (ev: BatteryStatusEvent) => any, useCapture?: boolean): void;
    /**
     * Removes a listener for an event from the BatteryStatus plugin.
     * @param Atype      - The event to stop listening for.
     * 
     *                     `batterystatus`: event fires when the percentage of battery charge changes by at least 1 percent, or if the device is plugged in or unplugged.
     *                    
     *                     `batterycritical`: event fires when the percentage of battery charge has reached the critical battery threshold. The value is device-specific.
     *                    
     *                     `batterylow`: event fires when the percentage of battery charge has reached the low battery threshold, device-specific value.
     * @param callback   - The function that executes when the event fires. The function is passed an BatteryStatusEvent object as a parameter.
     * @param useCapture - A Boolean indicating whether events of this type will be dispatched to the registered listener before being dispatched to any EventTarget beneath it in the DOM tree.
     */
    removeEventListener(type: batteryEvent, listener: (ev: BatteryStatusEvent) => any, useCapture?: boolean): void;
}

interface BatteryStatusEvent extends Event {
	/* The percentage of battery charge (0-100). */
    level: number;
	/* A boolean that indicates whether the device is plugged in. */
    isPlugged: boolean;
}
