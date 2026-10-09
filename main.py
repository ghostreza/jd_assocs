from flask import Flask, abort, render_template, send_from_directory

app = Flask(__name__)

PRODUCTS = {
    'sea-chariot-l380': {
        'name': 'SEA CHARIOT L380',
        'category': 'Marine',
        'image': 'seachariot_1.jpg',
        'gallery': ['seachariot_1.jpg', 'seachariot_2.jpg'],
        'tagline': 'Highly Maneuverable Commercial & Military Submersible (Max Depth: 20m)',
        'description': (
            'The SEA CHARIOT L380 is a highly maneuverable underwater vehicle suitable for commercial, '
            'military, and recreational tasks such as wreck hunting, photography, and marine biology. '
            'Designed to carry three people (two divers and one pilot) for an operational period of about '
            'three hours, it also offers an excellent stable platform for motion picture photography. '
            'The craft comes complete with an on-board air supply, depth gauge, and emergency buoyancy system.'
        ),
        'specs': {
            'Mechanical Specifications': [
                ('Operational Depth', '20 meters'),
                ('Capacity', '3 people (2 divers, 1 pilot) or 2 people + equipment'),
                ('Speed', '3 knots typical'),
                ('Buoyancy', 'Typically neutral with independent airbags for emergency ascent'),
                ('Construction', 'Reinforced fiberglass, 316 Stainless Steel, hard black anodized aluminium'),
                ('Colour Options', 'Graphite Black (RAL 9011) or Sulfur Yellow (RAL 1016)'),
                ('Environment', 'Military or Commercial')
            ],
            'Dimensions & Weight': [
                ('Overall Length', '3.8 meters'),
                ('Maximum Height', '0.7 meters'),
                ('Max Width (fins extended)', '1.80 meters'),
                ('Max Width (fins retracted)', '1.10 meters'),
                ('Weight in Air', 'Typically 250 Kg'),
                ('Air Supply', '4 x 15lt 200BAR tanks')
            ],
            'Electrical & Propulsion': [
                ('Operation Control', 'Spring loaded button switch Joy Stick'),
                ('Power Source', '36v 200ampH Lithium Battery Bank with full BMS protection (waterproof)'),
                ('Recharge Time', 'Less than 3 hours'),
                ('Operational Duration', '5 hours (at 3 knots) or 2 hours (at 4 knots)')
            ]
        },
        'standard_supply': [
            'Sea Chariot with 36v 200ampH Lithium Battery & BMS protection',
            'Depth Gauge & Compass',
            'Battery Status Indicators',
            '3 Air Cylinders and Contents Gauges',
            'Operator Manual',
            'Transportation Dolly'
        ],
        'extras': [
            'Transportation Trailer',
            'Underwater Lighting',
            'Underwater Night Vision',
            'Forward Looking Sonar',
            'GPS & Navigation Modules',
            'Navigation Lights',
            'Underwater Communications',
            'Special Custom Configurations (available upon consultation)'
        ]
    },
    'sea-chariot-mk3': {
        'name': 'SEA CHARIOT Mk3',
        'category': 'Marine',
        'image': 'seachariotmk3_1.jpg',
        'gallery': ['seachariotmk3_1.jpg', 'seachariotmk3_2.jpg'],
        'tagline': 'High-Performance Military Reconnaissance Submersible (Top Speed: 35 Knots)',
        'description': (
            'The SEA CHARIOT Mk3 is an underwater vehicle specially designed for military operations '
            'such as reconnaissance, with a maximum operational depth of 20 meters. This highly '
            'maneuverable submersible features a top surface speed of 35 knots and is designed to '
            'carry three people with their equipment for an underwater operational period of about '
            'four hours (alternatively, two people with an increased equipment load). It comes complete '
            'with an on-board microcomputer, instrumentation for monitoring surface and underwater '
            'propulsion, and communications between operators.'
        ),
        'specs': {
            'Mechanical Specifications': [
                ('Operational Depth', '20 meters (standard)'),
                ('Capacity', '3 people + equipment (or 2 people + increased equipment load)'),
                ('Environment', 'Military'),
                ('Construction', 'Carbon fiber, Reinforced fiberglass, Polymer & 316 Stainless Steel'),
                ('Colour', 'Graphite Black (RAL 9011) or to client’s request'),
                ('Buoyancy', 'Neutral with independent airbags for trim'),
                ('Life Support (Air)', '36,000 liters with manifold take off'),
                ('Air Bank (Re-inflation)', '5,000 liters plus air blower')
            ],
            'Dimensions & Weight': [
                ('Overall Length', '7.60 meters'),
                ('Maximum Height', '1.75 meters'),
                ('Max Width (hydroplanes extended)', '2.95 meters'),
                ('Max Width (hydroplanes retracted)', '2.60 meters'),
                ('Weight (less crew, cargo & fuel)', 'Approx. 1,750 Kg'),
                ('Operational Weight', '2,500 Kg typical')
            ],
            'Surface Propulsion': [
                ('Surface Power', '6-cylinder 260hp diesel engine & gearbox'),
                ('Maximum Surface Speed', 'Approx. 35 knots'),
                ('Typical Cruising Speed', '25 to 30 knots'),
                ('Operational Surface Range', '150 miles (subject to sea state and cargo)'),
                ('Surface Propulsion Type', 'Water jet'),
                ('Fuel Tank Capacity', '200 liters')
            ],
            'Electrical & Underwater Specifications': [
                ('Thrusters', '4 x 48vdc 5kv high performance brushless electrical motors'),
                ('Thruster Power Source', '48v 1,610 AmpH Lithium Ion Phosphate with BMS protection'),
                ('Underwater Speed', '3.5 knots (subject to prevailing current)'),
                ('Underwater Operational Duration', 'Approx. 4 hours'),
                ('Operation Control', 'Joystick'),
                ('Engine Starter Battery', '12v 100AmpH Lithium Iron Phosphate'),
                ('Recharge Time (Thrusters & Engine)', 'Approx. 3 hours'),
                ('Buoyancy Trim Inflation Blower', '48v 1800w (surface operation)')
            ]
        },
        'standard_supply': [
            'Sea Chariot complete with On-board microcomputer',
            'Digital Compass',
            'Battery Status Indicators',
            'Air Contents Gauges & Fuel Gauges',
            'Engine Temperature Gauges and Depth Finder',
            'Transport Dolly',
            'Operator Manual'
        ],
        'extras': [
            'Transport Trailer',
            'GPS Modules',
            'Forward Looking Sonar',
            'Special Navigation Modules',
            'Alternative instrumentation and support equipment (available on consultation)'
        ]
    },
    'patrol-boat-808': {
        'name': 'PATROL BOAT 808',
        'category': 'Craft for Sale',
        'image': 'patrolboat.jpg',
        'gallery': ['patrolboat.jpg'],
        'tagline': '17m GRP Patrol Craft for Police, Coast Guard, Diving, and Offshore Operations',
        'description': (
            'PATROL BOAT 808 is a 17-metre craft constructed from GRP and designed for Police or Coast Guard '
            'operations. It is also suitable for commercial diving or offshore oil exploration. Launched in '
            '1999, the vessel is reported to be in very good condition. The photograph shown is a patrol craft '
            'reference and is not confirmed as PATROL BOAT 808.'
        ),
        'specs': {
            'Physical Specifications': [
                ('Length Overall', '17.0 meters'),
                ('Beam Overall', '5.0 meters'),
                ('Designed Draft', '0.48 meters'),
                ('Designed Displacement', '2.80 meters'),
                ('Light Mass of Boat', '1.8 tons'),
                ('Total Mass of Boat', '3.40 tons'),
                ('Maximum Number of Passengers', '16 persons'),
                ('Minimum Crew', '2 persons'),
                ('Hull Construction', 'GRP'),
                ('Year Launched', '1999'),
                ('Reported Condition', 'Very good')
            ],
            'Propulsion Specifications': [
                ('Standard Engines', '2 x AIFO 8293 SRM 1000'),
                ('Fuel', 'Diesel'),
                ('Maximum Power', 'Not provided'),
                ('Maximum Surface Speed', '30 knots'),
                ('Cruising Speed', '25 knots')
            ]
        },
        'vessel_highlights': [
            'Designed for Police or Coast Guard operations',
            'Also suitable for commercial diving or offshore oil exploration',
            'The vessel information is given in good faith but without guarantee',
            'Offered subject to sale, price change, location change, or withdrawal without notice',
            'The displayed patrol craft photograph is for reference and is not confirmed as this vessel'
        ],
        'extras': []
    },
    'mv-quicksilver-vi': {
        'name': 'MV QUICKSILVER VI',
        'category': 'Marine',
        'image': 'mvquicksilverVI_1.jpg',
        'gallery': ['mvquicksilverVI_1.jpg'],
        'tagline': '38.6m Aluminium Catamaran (Currently in Jakarta, Indonesia)',
        'description': (
            'MV Quicksilver VI is a 38.6m aluminium constructed catamaran craft, currently lying in '
            'Jakarta, Indonesia. Built in Australia in 1989 by NQEA Pty Ltd (a premier engineering and '
            'shipbuilding company based in Cairns that has built vessels for the Royal Australian Navy '
            'and civilian sectors), she is currently fitted out for ferry and pleasure events. '
            'Classified by Det Norske Veritas, this robust vessel offers exceptional capacity and '
            'reliability for maritime transport and tourism.'
        ),
        'specs': {
            'General & Classification': [
                ('Name of Vessel', 'Quicksilver VI'),
                ('Call Sign', 'YETD'),
                ('Flag', 'Indonesia'),
                ('Port of Registry', 'Bali, Indonesia'),
                ('Classification', 'Det Norske Veritas'),
                ('Type', 'Catamaran'),
                ('Gross Tonnage', '176 tons'),
                ('DWT', '123 tons')
            ],
            'Dimensions & Capacity': [
                ('Length Overall (LOA)', '38.6 m'),
                ('Beam', '15.6 m'),
                ('Depth Molded', '4.49 m'),
                ('Draft Light', '1.4 m'),
                ('Draft Loaded', '1.6 m'),
                ('Crew Capacity', '11 persons'),
                ('Passenger Seats', '160 to 330')
            ],
            'Propulsion & Performance': [
                ('Main Engines', 'Detroit Marine Diesel Two Stroke 2 x 1195 KW V16'),
                ('Control', 'Electrical'),
                ('Starter', 'Air'),
                ('Reduction', '1:5'),
                ('Propulsion', 'Water Jet 2 x Kamewa ABS112'),
                ('Full Speed', '15 knots'),
                ('Fuel Consumption (Main)', '20 lts/hr')
            ],
            'Electrical & Auxiliary': [
                ('Auxiliary Engine/Generator', '2 x Perkins/Stamford 115HP/100kva, 3 phase, 50Hz'),
                ('Fuel Consumption (Aux)', '20 lts/hr standby')
            ],
            'Tank Capacities': [
                ('Fuel', '6,000 to 40,000 liters'),
                ('Lube Oil', '200 liters'),
                ('Fresh Water', '3,000 liters'),
                ('Grey Tank', '6,000 liters')
            ],
            'Safety & Layout': [
                ('Life Saving Equipment', '16 Carley Life rafts - 20 man capacity'),
                ('General Layout', 'Main Deck, Bridge Deck, Bridge, Sun Deck')
            ]
        },
        'vessel_highlights': [
            'Built by NQEA Australia (1989) - Builders of Royal Australian Navy vessels',
            'Classified by Det Norske Veritas',
            'Currently located in Jakarta, Indonesia',
            'Configured for Ferry and Pleasure Events',
            'High-capacity passenger seating (160 to 330 pax)'
        ],
        'extras': [
            'Ferry configuration',
            'Pleasure event configuration',
            'Custom refitting and modernization available upon consultation'
        ]
    },
    'night-watcher-m25': {
        'name': 'NIGHT WATCHER M25',
        'category': 'Electro-Optics',
        'image': 'NightWatcher25_1.jpg',
        'gallery': ['NightWatcher25_1.jpg', 'NightWatcher25_2.jpg', 'NightWatcher25_3.png'],
        'tagline': 'High-Performance Low-Cost Night Vision System',
        'description': (
            'The NIGHT WATCHER M25 is a high-performance, low-cost Night Vision System incorporating '
            'a 95mm Catadioptic Objective Lens and a 25mm 2nd Generation Image Intensifier, which is '
            'interchangeable with a 3rd Gen drop-in replacement. Ideally suitable for Law Enforcement, '
            'Border Control, Anti-Drug Operations, Animal Conservation, and similar tactical duties.'
        ),
        'specs': {
            'Mechanical Specifications': [
                ('Overall Length', '280mm (inc. OLC & eyeguard)'),
                ('Maximum Height', '112mm'),
                ('Maximum Width', '90mm'),
                ('Weight', '1.8 Kg'),
                ('Construction', 'Aluminium, hard black anodized (Optional Black Teflon finish)'),
                ('Environment', 'Commercial')
            ],
            'Optical Specifications': [
                ('Objective Lens', '95mm F/1.2 Catadioptic'),
                ('Field of View', '14.5 degrees (253 mr)'),
                ('Focus', '10m to Infinity'),
                ('Ocular Lens', '25mm (Fixed at -1.75 diopters)'),
                ('System Magnification', 'x3.8'),
                ('Range (Man-sized target)', '335m (Starlight)')
            ],
            'Electrical Specifications': [
                ('Image Intensifier', '25mm 2nd Generation MCP with AGC & BSP'),
                ('Tube Gain', '45,000 typical'),
                ('Tube Resolution', '28 lp/mm'),
                ('External Control', 'Combined rotary switch On/Off & Gain'),
                ('Power Source', '3.0 Lithium Battery (CR123A)'),
                ('Operational Duration', 'Approx. 30 hours')
            ]
        },
        'standard_supply': [
            'High Impact Carrying Case',
            'Operator’s Manual',
            'Lens Brush & Tissues',
            'Objective Lens Cap / Daylight Training Filter',
            'Open Eyeguard',
            'Lithium Batteries (x2)'
        ],
        'extras': [
            '3rd Gen Drop-in replacement Intensifier',
            '155mm Catadioptic Objective Lens',
            'High performance Objective Lenses',
            'Biocular Lens (Permits viewing with both eyes)',
            'Objective Lens Mount Adapters (For Photo Lenses)',
            'Relay Lenses for CCTV or 35mm SLR Cameras',
            'Pistol Grip',
            'Solid State Laser Illuminators',
            'Hostile Filters for 95mm & 155mm Objective Lenses',
            'Secured Eyeguard'
        ]
    },
    'night-seeker-mod-45135t': {
        'name': 'NIGHT SEEKER Mod-45135T',
        'category': 'Electro-Optics',
        'image': 'nightseekermod_1.jpg',
        'gallery': ['nightseekermod_1.jpg', 'nightseekermod_2.jpeg'],
        'tagline': 'Rugged Day/Night Thermal Observation System',
        'description': (
            'The NIGHT SEEKER Mod-45135T is a rugged Observation System (OS) designed for short to '
            'medium distances. Suitable for both Day and Night operations, it performs exceptionally '
            'well even under hazy or misty conditions. The system features a high-performance un-cooled '
            '8 to 14 micron microbolometer detector and a 45 to 135mm Germanium Objective Lens housed '
            'in a water-resistant aluminium casing.'
        ),
        'specs': {
            'Mechanical Specifications': [
                ('Overall Length', '260 mm'),
                ('Maximum Height', '170 mm'),
                ('Maximum Width', '150 mm'),
                ('Weight', '< 4.5 Kg'),
                ('Construction', 'Aluminium, black anodized with gloss white finish'),
                ('Environment', 'MIL SPEC'),
                ('Operating Temperature', '-20°C to +60°C'),
                ('Mounting', '¼” Whitworth')
            ],
            'Optical Specifications': [
                ('Objective Lens', '45 to 135mm F/1.0 Germanium Refractive'),
                ('Field of View (45mm)', '12˚ x 9˚'),
                ('Field of View (135mm)', '4˚ x 3'),
                ('Focus', '5m to infinity'),
                ('Detection Range (Man-sized)', '2,489 m'),
                ('Recognition Range (Man-sized)', '829 m')
            ],
            'Electrical Specifications': [
                ('Detector', '25µm pitch Microbolometer'),
                ('Spectral Range', '8 to 14 microns'),
                ('Number of Pixels', '384 x 288 / 320 x 240'),
                ('Frame Rate', '50Hz (60Hz for 320 x 240)'),
                ('Analog Video Output', 'CCIR or RS-170'),
                ('External Connection', '13pin Amphenol Connector to Control Unit'),
                ('External Controls', 'On/Off (Toggle), Digital Zoom, NUC, Video Polarity (Momentary Switches)'),
                ('Power Source 1', '12v DC (derived from Control Unit mains)'),
                ('Power Source 2 (Backup)', '1 x 7.2v 2200mAh Lithium Battery (BN-V812/814U)'),
                ('Operational Duration (Backup)', 'Approx. 4 hours'),
                ('Main Power Input', '90 to 230v AC')
            ]
        },
        'standard_supply': [
            'Hard Shell Carrying Case',
            'Operator’s Manual',
            'Objective Lens Cap'
        ],
        'extras': [
            'On-board Digital Compass',
            'GPS',
            'Solid State Laser Rangefinder',
            'Soft Carrying Bag',
            'Hardpoint Mounting'
        ]
    },
    'night-diver-model-dn': {
        'name': 'NIGHT DIVER Model-DN (Cyclops)',
        'category': 'Electro-Optics',
        'image': 'nightdiverdn_1.jpg',
        'gallery': ['nightdiverdn_1.jpg', 'nightdiverdn_2.jpg', 'nightdiverdn_3.jpg'],
        'tagline': 'High-Performance Underwater Night Vision Monocular Goggle',
        'description': (
            'The NIGHT DIVER Model-DN (Cyclops) is a high-performance Underwater Night Vision '
            'Monocular Goggle permitting observation both above and below water to a depth of 50 meters. '
            'Its modular design comprises a 25mm F/0.85 Objective Lens, a high-performance 2nd or 3rd '
            'Gen Image Intensifier with Battery and On/Off Switch, and a 25mm Ocular Lens. It is '
            'mounted on the Dräger Nova Full-face Mask, as used worldwide by many Navies, Special Forces, '
            'and Commandos. Ideal for above-water reconnaissance of beachhead defense installations and '
            'underwater searching of ship hulls or the seabed for explosive devices.'
        ),
        'specs': {
            'Mechanical Specifications': [
                ('Overall Length', '125mm outward projection'),
                ('Maximum Width', '180mm (subject to interpupillary adj.)'),
                ('Weight', '1.8 Kg in air'),
                ('Operational Depth', '50 meters'),
                ('Construction', 'Aluminium, hard black anodized with Black Teflon finish'),
                ('Environment', 'MIL SPEC')
            ],
            'Optical Specifications': [
                ('Objective Lens', '25mm F/0.85 Refractive'),
                ('Field of View', '40 degrees (above water)'),
                ('Focus', '30cm to Infinity'),
                ('Ocular Lens', '25mm'),
                ('Ocular Focus', '+/- 4 diopters'),
                ('Lateral Adjustment', 'approx. 7mm'),
                ('System Magnification', 'Unity'),
                ('Range (Man-sized target)', '150m (Starlight - above water)')
            ],
            'Electrical Specifications': [
                ('Image Intensifier', '18mm 2nd Gen / 18mm 3rd Gen'),
                ('Tube Sensitivity', '600µa/lm (2nd Gen) / 1,800µa/lm (3rd Gen)'),
                ('Tube Gain', '35,000 typical (2nd Gen) / 40,000 typical (3rd Gen)'),
                ('Tube Resolution', '60 lp/mm (2nd Gen) / 64 lp/mm (3rd Gen)'),
                ('External Control', 'Rotary switch – On/Off'),
                ('Power Source', '3.0 Lithium Battery (CR123A)'),
                ('Operational Duration', 'approx. 40 hours')
            ]
        },
        'standard_supply': [
            'High Impact Carrying Case',
            'Operator’s Manual',
            'Lens Brush & Tissues',
            'Objective Lens Caps or Daylight Training Filters'
        ],
        'extras': [
            'Selected High Performance Image Intensifiers (2nd & 3rd Generation)',
            'Solid State Laser Illuminators',
            'Soft Carrying Bag',
            'Super Visor permitting Illumination and CCTV systems to be mounted'
        ]
    },
    'night-diver': {
        'name': 'NIGHT DIVER',
        'category': 'Electro-Optics',
        'image': 'nightdiver_1.jpg',
        'gallery': ['nightdiver_1.jpg', 'nightdiver_2.png', 'nightdiver_3.jpg'],
        'tagline': 'Superior Underwater Night Vision Goggle',
        'description': (
            'The NIGHT DIVER is a superior Underwater Night Vision Goggle permitting observation '
            'both above and below water to a depth of 50 meters. The modular system comprises '
            'individual 25mm F/0.85 Objective Lenses, 2nd Gen or high performance 3rd Gen Image '
            'Intensifiers, and 25mm Ocular Lenses. It is mounted on the Interspiro Fullface Mask '
            'as used worldwide by many Navies, Special Forces, and Commandos. Ideal for above-water '
            'reconnaissance of Beachhead Defense Installations and underwater searching of ship hulls '
            'or the seabed for explosive devices.'
        ),
        'specs': {
            'Mechanical Specifications': [
                ('Overall Length', '125mm outward projection'),
                ('Maximum Width', '180mm (subject to interpupillary adj.)'),
                ('Weight', '1.8 Kg in air'),
                ('Operational Depth', '50 meters'),
                ('Construction', 'Aluminium, hard black anodized with Black Teflon finish'),
                ('Environment', 'MIL SPEC')
            ],
            'Optical Specifications': [
                ('Objective Lens', '25mm F/0.85 Refractive'),
                ('Field of View', '40 degrees (above water)'),
                ('Focus', '30cm to Infinity'),
                ('Ocular Lens', '25mm'),
                ('Ocular Focus', '+/- 4 diopters'),
                ('Interpupillary Adjustment', '54 to 72mm'),
                ('System Magnification', 'Unity'),
                ('Range (Man-sized target)', '150m (Starlight - above water)')
            ],
            'Electrical Specifications': [
                ('Image Intensifier', '18mm 2nd Gen / 18mm 3rd Gen'),
                ('Tube Sensitivity', '600µa/lm (2nd Gen) / 1,800µa/lm min (3rd Gen)'),
                ('Tube Gain', '35,000 typical (2nd Gen) / 40,000 typical (3rd Gen)'),
                ('Tube Resolution', '60 lp/mm (2nd Gen) / 64 lp/mm (3rd Gen)'),
                ('External Control', 'Rotary switch – On/Off'),
                ('Power Source', '2 x 3.0 Lithium Battery (CR123A)'),
                ('Operational Duration', 'approx. 40 hours')
            ]
        },
        'standard_supply': [
            'High Impact Carrying Case',
            'Operator’s Manual',
            'Lens Brush & Tissues',
            'Objective Lens Caps or Daylight Training Filters'
        ],
        'extras': [
            'High Performance 2nd or 3rd Gen SUPER Image Intensifiers',
            'Solid State Laser Illuminators (for close-up inspection)',
            'Soft Carrying Bag'
        ]
    },

    'night-shark': {
        'name': 'NIGHT SHARK',
        'category': 'Electro-Optics',
        'image': 'nightshark_1.jpg',
        'gallery': ['nightshark_1.jpg', 'nightshark_2.jpg', 'nightshark_3.png', 'nightshark_4.JPG'],
        'tagline': 'Compact Waterproof Handheld Night Vision System',
        'description': (
            'The NIGHT SHARK is a compact, waterproof, and extremely high-performance 2nd or 3rd '
            'Generation handheld Night Vision System designed for observation applications above and '
            'below water by Frogmen and Special Forces personnel. With a maximum operational depth '
            'of 50m and a 25mm F/0.85 Objective Lens, it permits clear images under most low light '
            'conditions.'
        ),
        'specs': {
            'Mechanical Specifications': [
                ('Overall Length', '150mm (inc. eyeguard)'),
                ('Maximum Height', '80mm'),
                ('Maximum Width', '58mm'),
                ('Weight', '0.76 Kg in air'),
                ('Construction', 'Aluminium, hard black anodized with Matt black teflon finish'),
                ('Environment', 'MIL SPEC'),
                ('Operational Depth', '50 meters')
            ],
            'Optical Specifications': [
                ('Objective Lens', '25mm F/0.85 Refractive'),
                ('Field of View', '42 degrees (720 mils)'),
                ('Focus', '30cm to Infinity'),
                ('System Magnification', 'Unity'),
                ('Range (Man-sized target)', '600m (Optimum Starlight Conditions)')
            ],
            'Electrical Specifications': [
                ('Image Intensifier', '18mm 2nd Gen / 18mm 3rd Gen'),
                ('Tube Sensitivity', '600µa/lm (2nd Gen) / 1,800µa/lm min (3rd Gen)'),
                ('Tube Gain', '35,000 typical (2nd Gen) / 40,000 typical (3rd Gen)'),
                ('Tube Resolution', '60 lp/mm (2nd Gen) / 64 lp/mm (3rd Gen)'),
                ('External Control', 'Rotary switch – On/Off'),
                ('Power Source', '2 x 3.0 Lithium Battery (CR123A)'),
                ('Operational Duration', 'approx. 40 hours')
            ]
        },
        'standard_supply': [
            'High Impact Carrying Case',
            'Operator’s Manual',
            'Lens Brush & Tissues',
            'Objective Lens Cap / Daylight Training Filter',
            'Open Eyeguard'
        ],
        'extras': [
            'High performance medium focal length Objective Lenses',
            'Sacrificial Filters for Objective Lenses',
            'Waterproof Solid State Laser Illuminators',
            'Soft Carrying Pouch'
        ]
    },

    'night-sentry-mk2': {
        'name': 'NIGHT SENTRY Mk2',
        'category': 'Electro-Optics',
        'image': 'nightsentry.jpg',
        'gallery': ['nightsentry.jpg', 'nightsentry_2.jpg', 'nightsentry_3.jpg'],
        'tagline': 'Modular Lightweight Monocular Night Vision System',
        'description': (
            'The NIGHT SENTRY Mk2 is a modular, lightweight, ultimate performance Monocular Night '
            'Vision System designed for application above and below water by Frogmen, Clearance '
            'Divers, or Special Forces. Its monocular design permits independent use of each eye, '
            'removing the serious problem of dark adjustment when using dual eye Night Vision Goggles. '
            'It incorporates a Selected High Performance 3rd Gen or 2nd Gen 18mm Image Intensifier '
            'and a 25mm F/0.95 Objective Lens. It can also be weapons mounted using the Elcan Weapons '
            'Mount on most small arms.'
        ),
        'specs': {
            'Mechanical Specifications': [
                ('Overall Length', '150mm (inc. eyeguard)'),
                ('Maximum Height', '110mm (inc. head mount clip)'),
                ('Maximum Width', '65mm'),
                ('Weight', '460 grs (without head harness)'),
                ('Construction', 'Aluminium, hard black anodized with Black Teflon finish'),
                ('Environment', 'MIL SPEC'),
                ('Operational Depth', '50 meters')
            ],
            'Optical Specifications': [
                ('Objective Lens', '25mm F/0.95 Refractive'),
                ('Field of View', '40 degrees (in air)'),
                ('Focus', '30cm to Infinity'),
                ('Ocular Lens', '26.5mm'),
                ('Ocular Focus', '+/- 4 diopters'),
                ('System Magnification', 'Unity'),
                ('Range (Man-sized target)', '150m (Starlight)')
            ],
            'Electrical Specifications': [
                ('Image Intensifier', '18mm 2nd Gen / 18mm 3rd Gen'),
                ('Tube Sensitivity', '600µa/lm (2nd Gen) / 1,800µa/lm (3rd Gen)'),
                ('Tube Gain', '35,000 typical (2nd Gen) / 40,000 typical (3rd Gen)'),
                ('Tube Resolution', '60 lp/mm (2nd Gen) / 64 lp/mm (3rd Gen)'),
                ('External Control', 'Rotary switch – On/Off'),
                ('Power Source', '3.0 Lithium Battery (CR123A)'),
                ('Operational Duration', 'Approx. 40 hours')
            ]
        },
        'standard_supply': [
            'High Impact Carrying Case',
            'Head Mount',
            'Operator’s Manual',
            'Lens Brush & Tissues',
            'Objective Lens Cap and Open Eyeguard'
        ],
        'extras': [
            'High performance Objective Lenses',
            'Auxiliary Magnifier Lens',
            'Daylight Training Filter',
            'Sacrificial Lens Ports for Objective Lenses',
            'Solid State Laser Illuminators and Weapon Mounts',
            'Modified Interspiro FFM for underwater operations'
        ]
    },
}

# SEO Meta Data
app.config['SEO'] = {
    'title': 'J&D Associates | Premier Defense, Security & Maritime Technologies',
    'description': 'J&D Associates delivers world-class night vision systems, high-performance underwater vehicles, and specialized naval vessels for defense and commercial applications.',
    'keywords': 'Night Vision, Sea Chariot, Underwater Vehicles, Defense Technology, Maritime Security, J&D Associates, Electro-Optics'
}

@app.context_processor
def inject_seo():
    return {'seo': app.config['SEO']}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/marine')
def marine():
    return render_template('marine.html', title='Marine: Sea Chariots & Vessels')

@app.route('/aviation')
def aviation():
    return render_template('aviation.html', title='Aviation: Aircraft & Spare Parts')

@app.route('/electro-optics')
def electro_optics():
    return render_template('electro_optics.html', title='Electro-Optics: Night Vision & Lighting')

@app.route('/craft-for-sale')
def craft_for_sale():
    return render_template('craft_for_sale.html', title='Craft for Sale | J&D Associates')

@app.route('/associates')
def associates():
    return render_template('associates.html', title='Associates | J&D Associates')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact J&D Associates')

@app.route('/product/<slug>')
def product_detail(slug):
    product = PRODUCTS.get(slug)
    if product is None:
        abort(404)
    return render_template('product_detail.html', product=product, title=f"{product['name']} | J&D Associates")

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(app.root_path, 'sitemap.xml', mimetype='application/xml')

@app.route('/robots.txt')
def robots():
    return send_from_directory(app.root_path, 'robots.txt', mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)