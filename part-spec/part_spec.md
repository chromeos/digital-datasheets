# key
## component type (fields should be listed in this order!)
* fieldName
    * definition of field
    * format
    * unit
    * json type
    * required/optional
    * automotive
    * non rohm compliant

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

# hardware
## switch
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* type
    * property describing the way in which the switch is activated
    * format: toggle, slide, rocker, push-button, etc.
    * type: string
    * optional
* contactType
    * property describing the order in which switch contact is made and broken
    * format: break-before-make, make-before-break
    * type: string
    * optional
* circuitConfig
    * property describing the number of poles and throws in a switch
    * format: SPST, SPDT, DPDT, DPST
    * type: string
    * optional
* cycleRating
    * number of on/off cycles a mechanical switch can reliably sustain
    * type: float
    * optional
* voltageRating
    * maximum DC voltage potential that can be applied across an open switch
    * unit: volts
    * type: float
    * optional
* currentRating
    * maximum DC current that can flow through a closed switch without causing excessive heating
    * unit: amps
    * type: float
    * optional
* onResistance
    * nominal resistance of a closed switch
    * unit: ohms
    * type: float
    * optional
* dielectricRating
    * maximum AC voltage potential that can be applied across an open switch for one minute
    * unit: volts
    * type: float
    * optional

## test point
* shape
    * shape of the test point
    * format: circle, square, oval
    * type: string
    * required
* length
    * longer dimension of a rectangular or oval test point
    * unit: mm
    * type: float
    * optional
* length
    * shorter dimension of a rectangular or oval test point
    * unit: mm
    * type: float
    * optional
* diameter
    * diameter of a circular test point
    * unit: mm
    * type: float
    * optional

## connector
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* function
    * intended function of a connector
    * format: headphone jack, USB-C, HDMI, etc.
    * type: string
    * optional
* contactCount
    * number of contacts in a connector
    * type: float
    * optional
* type
    * property describing the method of mating to the connector
    * format: plug, receptacle, header, jumper, etc.
    * type: string
    * optional
* cycleRating
    * number of plug/unplug cycles a connector is rated to support
    * type: float
    * optional
* zHeight
    * maximum height of a mounted connector from the PCB surface
    * unit: mm
    * type: float
    * optional
* pitch
    * distance from the center of one contact on the connector to the center of the next contact
    * unit: mm
    * type: float
    * optional
* keying
    * property describing whether a connector has an asymmetry to prevent it from being plugged in the wrong direction
    * format: yes, no
    * type: string
    * optional

# ic logic
## logic gate
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* type
    * logical operation performed by logic gate
    * format: and, or, nor, nand, inverter, buffer, configurable
    * type: string
    * required
* numberGates
    * number of logical gates encapsulated in logic IC
    * type: float
    * optional
* schmittTrigger
    * property describing whether logic gate has schmitt trigger inputs
    * format: yes, no
    * type: string
    * optional
* propagationDelay
    * time between input changing to output changing
    * unit: seconds
    * type: float
    * optional

## clock
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* fixedFrequency
    * clock frequency value if the clock has a fixed frequency
    * unit: Hz
    * type: float
    * optional
* minFrequency
    * minimum clock frequency value if the clock has a configurable frequency
    * unit: Hz
    * type: float
    * optional
* maxFrequency
    * maximum clock frequency value if the clock has a configurable frequency
    * unit: Hz
    * type: float
    * optional
* numberClockOutputs
    * number of clock outputs in a clock IC
    * type: float
    * optional
* diffSingleEnded
    * property describing whether a clock output is single ended or differential
    * format: diff, single
    * type: string
    * optional
* jitter
    * cycle to cycle clock jitter
    * unit: seconds
    * type: float
    * optional
* frequencyTolerance
    * amount of frequency variation specced from nominal frequency
    * unit: percentage
    * type: float
    * optional
* psrr
    * power supply rejection ratio or ratio between power supply variation and output variation
    * unit: dB
    * type: float
    * optional
* outputFormat
    * signal format of clock output
    * format: lvpecl, lvds, hcsl, etc.
    * type: string
    * optional

## power sequencing
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* targetApplication
    * description of intended power sequencing chip application (example: KBL SOC, LPDDR4 memory, etc.)
    * type: string
    * optional
* fixedConfigurable
    * description of whether a power sequencing IC has fixed or configurable logic
    * format: fixed, configurable
    * type: string
    * optional

# ic misc
## speaker amplifier
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* dataLength
    * number of bits in a data word
    * type: float
    * optional
* outputPower
    * typical output power from speaker amplifier
    * unit: watts
    * type: float
    * optional
* outputPowerConditions
    * decription of voltage and load conditions under which output power is measured
    * format: (example) 4 ohms at 5V
    * type: string
    * optional
* efficiency
    * typical speaker amplifier efficiency
    * unit: percentage
    * type: float
    * optional
* efficiencyConditions
    * description of load and THD+N conditions under which efficiency is measured
    * format: (example) Rl = 8ohms, THD+N = 10%
    * type: string
    * optional
* thd+n
    * typical total harmonic distortion plus noise of amplifier
    * unit: percentage
    * type: float
    * optional
* thd+nConditions
    * description of frequency, power, and load conditions under which thd+n is measured
    * format: (example) f = 1kHz, pout = 1W, z speaker = 4ohms + 33uH
    * type: string
    * optional
* sampleRate
    * sample rate of data out of amplifier
    * unit: Hz
    * type: float
    * optional
* interface
    * describes the communication interface from the chip to the host
    * format: i2s, soundwire, etc.
    * type: string
    * optional

## audio codec
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* dataLength
    * number of bits in a data word
    * type: float
    * optional
* hpOutputSNR
    * headphone amplifier output SNR
    * unit: dB
    * type: float
    * optional
* hpOutputTHD+N
    * headphone output total harmonic distortion plus noise
    * unit: percentage
    * type: float
    * optional
* micInputSNR
    * microphone input SNR
    * unit: dB
    * type: float
    * optional
* micInputTHD+N
    * microphone input total harmonic distortion plus noise
    * unit: percentage
    * type: float
    * optional
* jackDetect
    * describes whether headphone jack detection is supported
    * format: yes, no
    * type: string
    * optional
* interface
    * describes the communication interface from the chip to the host
    * format: i2s, soundwire, etc.
    * type: string
    * optional

## wlan module
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* wlanSpec
    * version of wlan specification supported by module
    * format: 802.11ac, 802.11ax, etc.
    * type: string
    * optional
* bluetoothVersion
    * version of bluetooth supported by module
    * format: 4.0, 4.1, 5.0, etc.
    * type: string
    * optional
* txrxChains
    * number of tx and rx chains in a wifi module
    * format: 2x2, 2x1, etc.
    * type: string
    * optional
* m2FormFactor
    * wlan module form factor described by jedec standard m.2 form factors
    * format: 1216, 2230, etc.
    * type: string
    * optional
* keying
    * pcie card key
    * format: E, hybrid-E, etc.
    * type: string
    * optional
* lteCoexFilter
    * describes whether module supports lte coexistance filtering
    * format: yes, no
    * type: string
    * optional
* interface
    * describes the communication interface from the chip to the host
    * format: pcie, cnvi, etc.
    * type: string
    * optional

## wwan module
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* networkSupport
    * networks supported by wwan module
    * format: [3G, 4G, 5G]
    * type []string
    * optional
* gpsSupport
    * whether wwan module has gps support
    * format: yes, no
    * type: string
    * optional
* m2FormFactor
    * wlan module form factor described by jedec standard m.2 form factors
    * format: 3042
    * type: string
    * optional
* keying
    * pcie card key
    * format: B, etc.
    * type: string
    * optional
* interface
    * describes the communication interface from the chip to the host
    * format: pcie, usb3, etc.
    * type: string
    * optional

## tpm
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* interface
    * describes the communication interface from the chip to the host
    * format: spi, i2c, lpc,
    * type: string
    * optional

# ic micro
## microcontroller/ec/asic
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* onChipFlash
    * quantity of built-in flash in a microprocessor
    * unit: KB
    * type: float
    * optional
* onChipRAM
    * quantity of built-in RAM in a microprocessor
    * unit: KB
    * type: float
    * optional
* interfaces
    * list of supported interfaces in a microprocessor
    * format: [i2c, spi, uart, espi, etc.]
    * type: []string
    * optional
* coreProcessor
    * description of core processor
    * format: 32-bit ARM Cortex-M4
    * type: string
    * optional

# ic io
## usb-c port controller
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* pdVersion
    * version of power delivery spec implemented by controller
    * format: pd2, pd3
    * type: string
    * optional
* vconnPowerSupport
    * whether controller has support for vconn power
    * format: yes, no
    * type: string
    * optional
* vconnPowerLimit
    * power limit supported by internal vconn switch (if supported)
    * unit: watts
    * type: float
    * optional

## bc12
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* hostMode
    * whether host mode is supported by bc12 chip
    * format: yes, no
    * type: string
    * optional
* deviceMode
    * whether device mode is supported by bc12 chip
    * format: yes, no
    * type: string
    * optional

## pd power mux
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* fastRoleSwap
    * whether fast role swap is supported
    * format: yes, no
    * type: string
    * optional
* ccIsolation
    * whether cc pins can be isolated through an internal switch
    * format: yes, no
    * type: string
    * optional
* deadBatteryMode
    * whether dead battery mode is supported on cc pins
    * format: yes, no
    * type: string
    * optional
* reverseCurrentBlocking
    * whether vbus power path supports reverse current blocking
    * format: yes, no
    * type: string
    * optional
* ocp
    * over current protection limit provided on vbus power path
    * unit: amps
    * type: float
    * optional
* ovp
    * over voltage protection limit provided on vbus power path
    * unit: volts
    * type: float
    * optional

## usb-c redriver/retimer
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* auxMux
    * whether chip supports internal muxing of aux pins
    * format: yes, no
    * type: string
    * optional
* usbVersion
    * highest version of usb spec supported by redriver/retimer
    * format: 2.0, 3.1, 3.1 gen2, 4.0
    * type: string
    * optional
* dpVersion
    * highest version of dp spec supported by redriver/retimer
    * format: hbr2, hbr3
    * type: string
    * optional
* tbtVersion
    * highest version of thunderbolt spec supported by redriver/retimer
    * format: 2, 3, 4
    * type: string
    * optional
* pcieVersion
    * highest version of pcie spec supported by redriver/retimer
    * format: gen2, gen3
    * type: string
    * optional

## usb-c mux
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* vconnPowerSupport
    * whether controller has support for vconn power
    * format: yes, no
    * type: string
    * optional
* vconnPowerLimit
    * power limit supported by internal vconn switch (if supported)
    * unit: watts
    * type: float
    * optional
* redriving
    * whether a mux includes redriving support
    * format: yes, no
    * type: string
    * optional
* auxMux
    * whether chip supports internal muxing of aux pins
    * format: yes, no
    * type: string
    * optional
* usbVersion
    * highest version of usb spec supported by redriver/retimer
    * format: 2.0, 3.1, 3.1 gen2, 4.0
    * type: string
    * optional
* dpVersion
    * highest version of dp spec supported by redriver/retimer
    * format: hbr2, hbr3
    * type: string
    * optional
* tbtVersion
    * highest version of thunderbolt spec supported by redriver/retimer
    * format: 2, 3, 4
    * type: string
    * optional
* pcieVersion
    * highest version of pcie spec supported by redriver/retimer
    * format: gen2, gen3
    * type: string
    * optional

## usb-c mux/port controller
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* pdVersion
    * version of power delivery spec implemented by controller
    * format: pd2, pd3
    * type: string
    * optional
* vconnPowerSupport
    * whether controller has support for vconn power
    * format: yes, no
    * type: string
    * optional
* vconnPowerLimit
    * power limit supported by internal vconn switch (if supported)
    * unit: watts
    * type: float
    * optional
* redriving
    * whether a mux includes redriving support
    * format: yes, no
    * type: string
    * optional
* auxMux
    * whether chip supports internal muxing of aux pins
    * format: yes, no
    * type: string
    * optional
* usbVersion
    * highest version of usb spec supported by redriver/retimer
    * format: 2.0, 3.1, 3.1 gen2, 4.0
    * type: string
    * optional
* dpVersion
    * highest version of dp spec supported by redriver/retimer
    * format: hbr2, hbr3
    * type: string
    * optional
* tbtVersion
    * highest version of thunderbolt spec supported by redriver/retimer
    * format: 2, 3, 4
    * type: string
    * optional
* pcieVersion
    * highest version of pcie spec supported by redriver/retimer
    * format: gen2, gen3
    * type: string
    * optional

## redriver
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* numberChannels
    * number of lanes (single ended or differential) supported by redriver
    * type: float
    * optional
* interface
    * list of interface(s) supported by redriver
    * format: [hdmi2, dp hbr3, usb3.1 gen2]
    * type: []string
    * optional
* maxDataRate
    * maximum data rate supported by redriver
    * unit: Hz
    * type: float
    * optional

## bridge chip
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* muxRatio
    * ratio of inputs to outputs
    * format: 2:1, 1:1, etc.
    * type: string
    * optional
* inputInterfaces
    * list of interfaces at the input of the bridge
    * format: [hdmi2.0, dp hbr2]
    * type: []string
    * optional
* outputInterfaces
    * list of interfaces at the output of the bridge
     * format: [dp hbr2]
    * type: []string
    * optional

## level shifter
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* numberChannels
    * number of lanes (single ended or differential) supported by redriver
    * type: float
    * optional
* interface
    * interface supported by redriver
    * format: hdmi1.4, hdmi2.0, etc.
    * type: string
    * optional
* inputVoltage
    * input voltage level of level shifter
    * unit: volts
    * type: float
    * optional
* outputVoltage
    * output voltage level of level shifter
    * unit: volts
    * type: float
    * optional

# sensor
## accelerometer
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* accelerationRanges
    * range of force that accelerometer can measure
    * format: [2, 4, 8, 16]
    * unit: g
    * type: []float
    * optional
* sensitivity
    * smallest change in force accelerometer is able to capture (typical). Corresponds to levels in acceleration ranges
    * format: [16000, 8000, 4000, 2000]
    * unit: LSB/g
    * type: []float
    * optional
* axis
    * number of axes of acceleration measurement
    * type: float
    * optional
* interface
    * interface(s) for communication to host
    * format: [i2c, spi, analog]
    * type: []string
    * optional
* bandwidth
    * bandwidth of acceleration measurement
    * unit: Hz
    * type: float
    * optional

## accelerometer/gyro
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* accelerationRanges
    * range of force that accelerometer can measure
    * format: [2, 4, 8, 16]
    * unit: g
    * type: []float
    * optional
* accelerationSensitivity
    * smallest change in force accelerometer is able to capture (typical). Corresponds to levels in acceleration ranges
    * format: [16000, 8000, 4000, 2000]
    * unit: LSB/g
    * type: []float
    * optional
* gyroRanges
    * range of angular speed that gyro can measure
    * format: [125, 250, 500]
    * unit: degrees-per-second (dps)
    * type: []float
    * optional
* gyroSensitivity
    * smallest change in angular speed gyro is able to capture (typical). Corresponds to levels in gyro ranges
    * format: [16, 32, 65]
    * unit: LSB/dps
    * type: []float
    * optional
* axis
    * number of axes of measurement
    * type: float
    * optional
* interface
    * interface(s) for communication to host
    * format: [i2c, spi, analog]
    * type: []string
    * optional

## magnetic sensor
* type
    * method by which magnetism is detected
    * format: gmr, hall effect
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
* trip
    * magnetic threshold causing the sensor to output high
    * unit: mT
    * type: float
    * optional
* release
    * magnetic threshold causing the sensor to output low
    * unit: mT
    * type: float
    * optional

## thermal
* type
    * method by which temperature is detected
    * format: rtd, thermistor, silicon bandgap
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
* interface
    * interface(s) for communication to host
    * format: [i2c, spi, analog]
    * type: []string
    * optional
* resolution
    * maximum resolution of temperature sensor
    * unit: degreesC/LSD
    * type: float
    * optional

# storage/memory
## ssd
* type
    * type of ssd storage as defined by interface and technology
    * format: emmc, sata, nvme
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
* capacity
    * capacity of SSD
    * unit: GB
    * type: float
    * required
* dataRate
    * maximum data rate
    * unit: GB/sec
    * type: float
    * optional
* interface
    * interface of ssd to host
    * format: emmc 5.1, pcie gen3, etc.
    * type: string
    * optional

## sd card reader
* type
    * type of sd card reader
    * format: micro, full size
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

## dram
* type
    * type of dram
    * format: lpddr3, ddr3, lpddr4, lpddr4x, ddr4, lpddr5, ddr5
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
* capacity
    * capacity of dram chip
    * unit: Gb
    * type: float
    * required
* speed
    * dram maximum speed
    * unit: Mbps
    * type: float
    * optional

## rom
* manufacturer
    * company that manufacturers the part
    * type: string
    * required
* mpn
    * manufacturer part number
    * type: string
    * required
* capacity
    * capacity of rom
    * unit: Mb
    * type: float
    * required
* interface
    * interace of rom to host
    * format: spi, i2c
    * type: string
    * required
* qeStatus
    * indicates whether the QE bit is set
    * format: yes, no
    * type: string
    * optional

