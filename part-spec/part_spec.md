# key
## component type (fields should be listed in this order!)
* fieldName
    * definition of field
    * format
    * unit
    * json type
    * required/optional
    * automotive

# passives
## resistor
* tolerance
    * nominal tolerance of a resistor
    * unit: %
    * type: float
    * required
* powerRating
    * measure of power a resistor can dissipate indefinitely without degrading performance
    * unit: watts
    * type: float
    * optional
* package
    * package size of resistor
    * format: 0201, 2.0x1.0x0.5
    * type: string
    * optional
* packageFormat
    * format used for expressing package code
    * format: metric, imperial, length(mm)xwidth(mm)xheight(mm)
    * type: string
    * optional (required if package is listed)
* value
    * resistance value expressed as a float
    * unit: ohms
    * type: float
    * required
* humanValue
    * resistance value expressed with metric prefix
    * unit: ohms
    * type: string
    * optional

## capacitor
* package
    * package size of capacitor
    * format: 0201, 2.0x1.0x0.5
    * type: string
    * optional
* packageFormat
    * format used for expressing package code
    * format: metric, imperial, length(mm)xwidth(mm)xheight(mm)
    * type: string
    * optional (required if package is listed)
* value
    * capacitance value
    * unit: farads
    * type: float
    * required
* humanValue
    * capacitance value expressed with metric prefix
    * unit: farads
    * type: string
    * optional
* tolerance
    * nominal tolerance of a capacitor
    * unit: %
    * type: float
    * optional
* ratedVoltage
    * maximum voltage which may be applied continuously to a capacitor
    * unit: volts
    * type: float
    * required
* dielectric
    * dielectric material in a fixed capacitor
    * format: ceramic, C0G, NP0, X7R, Y5V, Z5U, electrolytic, tantalum, plasticFilm
    * type: string
    * optional
* polarized
    * whether a capacitor is polarized
    * format: yes, no
    * type: string
    * optional
* esr
    * equivalent series resistance of a capacitor
    * unit: ohms
    * type: float
    * optional
* maxTemp
    * maximum temperature under which a capacitor can be expected to reliably operate
    * unit: degrees C
    * type: float
    * optional
* minTemp
    * minimum temperature under which a capacitor can be expected to reliably operate
    * unit: degrees C
    * type: float
    * optional

## inductor
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* package
    * package size of inductor
    * format: 0201, 2.0x1.0x0.5
    * type: string
    * optional
* packageFormat
    * format used for expressing package code
    * format: metric, imperial, length(mm)xwidth(mm)xheight(mm)
    * type: string
    * optional (required if package is listed)
* value
    * inductance value
    * unit: henries
    * type: float
    * required
* humanValue
    * inductance value expressed with metric prefix
    * unit: henries
    * type: string
    * optional
* tolerance
    * nominal tolerance of inductor
    * unit: %
    * type: float
    * optional
* isat
    * saturation current or the applied DC current at which inductance drops below a specified level, typically 30% of the specced inductance
    * unit: amps
    * type: float
    * optional
* irms
    * applied DC current that produces an inductor temperature rise of 40 deg C
    * unit: amps
    * type: float
    * optional
* dcr
    * dc resistance of an inductor
    * unit: ohms
    * type: float
    * optional
* acr
    * ac resistance of an inductor at various frequency points
    * type: dictionary<float><float>
    * format: dictionary<frequency><AC resistance>
    * unit: dictionary<Hz><ohms>
    * optional

## common mode choke
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* package
    * package size of common mode choke
    * format: 0201, 2.0x1.0x0.5
    * type: string
    * optional
* packageFormat
    * format used for expressing package code
    * format: metric, imperial, length(mm)xwidth(mm)xheight(mm)
    * type: string
    * optional (required if package is listed)
* diffModeCutoff
    * frequency at which the differential mode attenuation equals -3dB
    * unit: Hz
    * type: float
    * optional
* commonModeAttenuation
    * common mode attenuation of a common mode choke at various frequencies
    * format: dictionary<frequency><attenuation>
    * unit: dictionary<Hz><dB>
    * type: dictionary<float><float>
    * optional
* dcr
    * dc resistance of a common mode choke
    * unit: ohms
    * type: float
    * optional
* irms
    * applied DC current that produces a common mode choke temperature rise of 40 deg C
    * unit: amps
    * type: float
    * optional
* intendedApplication
    * intended application of a particular common mode choke
    * format: [USB2.0, USB3.0, LVDS]
    * type: []string
    * optional

## ferrite bead
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* package
    * package size of ferrite bead
    * format: 0201, 2.0x1.0x0.5
    * type: string
    * optional
* packageFormat
    * format used for expressing package code
    * format: metric, imperial, length(mm)xwidth(mm)xheight(mm)
    * type: string
    * optional (required if package is listed)
* dcr
    * dc resistance of ferrite bead
    * unit: ohms
    * type: float
    * optional
* irms
    * applied DC current that produces a ferrite bead temperature rise of 40 deg C
    * unit: amps
    * type: float
    * optional
* impedance100MHz
    * impedance of ferrite bead under standard testing conditions at 100MHz
    * unit: ohms
    * type: float
    * optional
* impedanceTolerance
    * variation of ferrite bead impedance expressed as +/- percentage
    * unit: percentage
    * type: float
    * optional

# semiconductor
## transistor
* type
    * type of transistor
    * format: mosfet, bjt, jfet, etc.
    * type: string
    * required
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* channel
    * doping of a transistor's channel - describes whether a transistor is n-type or p-type
    * format: nType, pType
    * unit: string
    * required
* vgsMax
    * maximum gate to source voltage difference that can be continously applied to a mosfet
    * unit: volts
    * type: float
    * optional
* vdsMax
    * maximum drain to source voltage difference that can be continously applied to a mosfet
    * unit: volts
    * type: float
    * optional
* vgsThMax
    * maximum gate to source voltage difference required to produce a conducting path between drain and source
    * unit: volts
    * type: float
    * optional
* iDrain
    * maximum continous DC current that can flow through a mosfet channel
    * unit: amps
    * type: float
    * optional
* idPulsed
    * maximum pulsed DC current that can flow through a mosfet channel
    * unit: amps
    * type: float
    * optional
* rdson
    * drain source on resistance of a mosfet
    * unit: ohms
    * type: float
    * optional
* rdsonCondition
    * description of the gate-source voltage and drain current under which rdson is measured
    * format: "vgs = 2.5V, id = 1A"
    * type: string
    * optional
* qg
    * total gate charge of a mosfet
    * unit: nC
    * type: float
    * optional
* qgd
    * gate to drain charge of a mosfet
    * unit: nC
    * type: float
    * optional
* qgs
    * gate to source charge of a mosfet
    * unit: nC
    * type: float
    * optional
* chargeCondition
    * description of the drain-source voltage and drain current under which gate charge is measured
    * format: "vds = 6V, id = 1A"
    * type: string
    * optional

## diode
* type
    * type of diode
    * format: zener, schottky, esd
    * type: string
    * required
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* vf
    * forward voltage of a diode
    * unit: volts
    * type: float
    * optional
* vfCondition
    * forward current of diode under which a given forward voltage was measured
    * unit: amps
    * type: float
    * optional, required if vf is present
* ifm
    * maximum continuous forward current a diode can support
    * unit: amps
    * type: float
    * optional
* ifrm
    * maximum repetitive peak forward current a diode can support
    * unit: amps
    * type: float
    * optional
* ifsm
    * maximum non-repetitive surge forward current a diode can support
    * unit: amps
    * type: float
    * optional
* vbr
    * breakdown voltage of a diode
    * unit: volts
    * type: float
    * optional
* ir
    * reverse leakage current
    * unit: amps
    * type: float
    * optional
* irCondition
    * reverse bias voltage under which reverse leakage current occurs
    * unit: volts
    * type: float
    * optional, required if reverse leakage current is listed
* vz
    * breakdown voltage of a zener diode
    * unit: volts
    * type: float
    * optional
* vzCondition
    * minimum reverse current condition under which breakdown voltage of a zener diode is achieved
    * unit: amps
    * type: float
    * optional
* vrm
    * reverse standoff voltage of a tvs diode
    * unit: volts
    * type: float
    * optional
* vcl
    * clamping voltage of a tvs diode
    * unit: volts
    * type: float
    * optional
* vclCondition
    * surge current condition under which a tvs clamping voltage occurs
    * unit: amps
    * type: float
    * optional
* esdProtection
    * whether a diode has built in esd protection
    * format: yes, no
    * type: string
    * optional

# power
## ldo
* type
    * ldo type
    * format: fixed, adjustable
    * type: string
    * required
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* vinMin
    * minimum input voltage under which the part can be expected to operate properly
    * unit: volts
    * type: float
    * optional
* vinMax
    * maximum input voltage under which the part can be expected to operate properly
    * unit: volts
    * type: float
    * optional
* dropoutVoltage
    * nominal dropout voltage for ldo
    * unit: volts
    * type: float
    * optional
* ilim
    * maximum sustained current output current under which the part will operate properly
    * unit: amps
    * type: float
    * optional
* turnOnTime
    * time for output voltage to go from 10% vout nominal to 90% vout nominal
    * unit: seconds
    * type: float
    * optional

## voltage regulator
* type
    * switching voltage regulator type
    * format: buck, boost, buck-boost, other
    * type: string
    * required
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* vinMin
    * minimum input voltage under which the part can be expected to operate properly
    * unit: volts
    * type: float
    * optional
* vinMax
    * maximum input voltage under which the part can be expected to operate properly
    * unit: volts
    * type: float
    * optional
* voutMin
    * minimum output voltage part can regulate
    * unit: volts
    * type: float
    * optional
* voutMax
    * maximum output voltage part can regulate
    * unit: volts
    * type: float
    * optional
* fsw
    * swtiching frequency of voltage regulator
    * unit: hertz
    * type: []float
    * optional
* ilim
    * maximum sustained current output current under which the part will operate properly
    * unit: amps
    * type: float
    * optional
* turnOnTime
    * time for output voltage to go from 10% vout nominal to 90% vout nominal
    * unit: seconds
    * type: float
    * optional
* integratedFets
    * whether the regulator contains integrated switching mosfets
    * format: yes, no
    * type: string
    * optional

## load switch
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* vinMin
    * minimum input voltage under which the part can be expected to operate properly
    * unit: volts
    * type: float
    * optional
* vinMax
    * maximum input voltage under which the part can be expected to operate properly
    * unit: volts
    * type: float
    * optional
* ilim
    * maximum sustained current output current under which the part will operate properly
    * unit: amps
    * type: float
    * optional
* turnOnTimeNominal
    * nominal time for output voltage to go from 10% vout nominal to 90% vout nominal for fixed turn-on time part
    * unit: seconds
    * type: float
    * optional
* turnOnTimeMin
    * minimum time for output voltage to go from 10% vout nominal to 90% vout nominal for variable turn-on time part
    * unit: seconds
    * type: float
    * optional
* turnOnTimeMax
    * minimum time for output voltage to go from 10% vout nominal to 90% vout nominal for variable turn-on time part
    * unit: seconds
    * type: float
    * optional
* reverseCurrentBlocking
    * whether load switch has capability to block current flow from vout to vin
    * format: yes, no
    * type: string
    * optional
* onResistance
    * nominal DC resistance of load switch when enabled
    * units: ohms
    * type: float
    * optional

## battery charger
* converterType
    * switching voltage regulator type
    * format: buck, boost, buck-boost, other
    * type: string
    * required
* chargerTopology
    * type of battery charger topology (Narrow VDC vs Hybrid Power Boost)
    * format: nvdc, hpb
    * type: string
    * optional
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* batteryConfig
    * battery serial configurations supported by charger
    * format: 1S, 2S, 3S, 4S
    * type: []string
    * required
* vinMin
    * minimum input voltage under which the part can be expected to operate properly
    * unit: volts
    * type: float
    * optional
* vinMax
    * maximum input voltage under which the part can be expected to operate properly
    * unit: volts
    * type: float
    * optional
* voutMin
    * minimum output voltage part can regulate
    * unit: volts
    * type: float
    * optional
* voutMax
    * maximum output voltage part can regulate
    * unit: volts
    * type: float
    * optional
* fsw
    * swtiching frequency of voltage regulator
    * unit: hertz
    * type: []float
    * optional
* ilim
    * maximum sustained current output current under which the part will operate properly
    * unit: amps
    * type: float
    * optional
* TCPCSupport
    * whether type-C port controller support is built in
    * format: yes, no
    * type: string
    * optional
* BC12Support
    * whether bc 1.2 detection is built in
    * format: yes, no
    * type: string
    * optional
* itegratedLoadSwitch
    * whether the charger contains integrated power path load switch(es)
    * format: yes, no
    * type: string
    * optional
* integratedFets
    * whether the charger contains integrated switching mosfets
    * format: yes, no
    * type: string
    * optional

## display backlight driver
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* vinMin
    * minimum input voltage under which the part can be expected to operate properly
    * unit: volts
    * type: float
    * optional
* vinMax
    * maximum input voltage under which the part can be expected to operate properly
    * unit: volts
    * type: float
    * optional
* voutMin
    * minimum output voltage part can regulate
    * unit: volts
    * type: float
    * optional
* voutMax
    * maximum output voltage part can regulate
    * unit: volts
    * type: float
    * optional
* fsw
    * swtiching frequency of voltage regulator
    * unit: hertz
    * type: []float
    * optional
* ilim
    * maximum sustained current output current under which the part will operate properly
    * unit: amps
    * type: float
    * optional
* integratedFets
    * whether the charger contains integrated switching mosfets
    * format: yes, no
    * type: string
    * optional
* currentMatchingAccuracy
    * current matching between LED strings
    * unit: percentage
    * type: float
    * optional
* numberLEDStrings
    * maximum number of LED strings supported by display driver
    * type: float
    * optional

## PMIC
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* targetApplication
    * description of intended PMIC application (example: KBL SOC, LPDDR4 memory, etc.)
    * type: string
    * optional
* numIntegratedFetOutput
    * number of switching DC-DC converters with integrated mosfets in PMIC
    * type: float
    * optional
* numExternalFetOutput
    * number of switching DC-DC converters with external mosfets in PMIC
    * type: float
    * optional
* numLDO
    * number of integrated LDOs in PMIC
    * type: float
    * optional
* numLoadSwitch
    * number of integrated load switches in PMIC
    * type: float
    * optional
* vinMin
    * minimum input voltage under which the part can be expected to operate properly
    * unit: volts
    * type: float
    * optional
* vinMax
    * maximum input voltage under which the part can be expected to operate properly
    * unit: volts
    * type: float
    * optional
* interface
    * communication interface to host device
    * format: i2c, spi, enables, etc.
    * type: float
    * optional