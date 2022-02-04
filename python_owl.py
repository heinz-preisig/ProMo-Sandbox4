

#!/usr/local/bin/python3
# encoding: utf-8

"""
===============================================================================
 Ontology design facility
===============================================================================

This program is part of the ProcessModelling suite

"""

__project__ = "ProcessModeller  Suite"
__author__ = "PREISIG, Heinz A"
__copyright__ = "Copyright 2015, PREISIG, Heinz A"
__since__ = "16.09.2019"
__license__ = "GPL planned -- until further notice for Bio4Fuel & MarketPlace internal use only"
__version__ = "5.04"
__email__ = "heinz.preisig@chemeng.ntnu.no"
__status__ = "beta"


import sys
import os

ProMo_path = os.path.join("../../","ProMo")



root = os.path.abspath(ProMo_path)      #os.path.join("../../"{{ProMo}}) #ProcessModeller_v7_04"))

ext = [root, os.path.join(root, 'packages'), \
             os.path.join(root, 'tasks'), \
             os.path.join(root, 'packages', 'OntologyBuilder', 'EMMO_Integration')
       ]
# print(os.path.join(root, 'packages', 'OntologyBuilder', 'EMMO_Integration'))

# emmo = "/home/heinz/1_Gits/ProcessModeller/ProcessModeller_v7_04/packages/OntologyBuilder/EMMO_Integration/"

sys.path.extend(ext)
from OntologyBuilder.EMMO_Integration.emmo_attach import ProMoOwlOntology
from Common.ontology_container import OntologyContainer

from owlready2 import *

ontology = OntologyContainer("ProMo_sandbox4") #'flash_03')


variables = ontology.variables

name = "play"
owlfile = name+".owl"

# onto  = O.setup_ontology(name)
o = ProMoOwlOntology()
onto = o.setupOnto()

with onto:
  class ProMoVar(onto.VAR):
    pass

  class has_function(ObjectProperty):
    domain = [ProMoVar]
    range  = [ProMoVar]
    pass

  class function(Thing):
    domain  = [ProMoVar]
    range   = [ProMoVar]
    pass

  class is_function_of(ObjectProperty):
    domain = [ProMoVar]
    range  = [ProMoVar]
    pass

# 1
label = variables[1]["label"]
network = variables[1]["network"]
variable_type = variables[1]["type"]
label = variables[1]["label"]
doc = variables[1]["doc"]
onto_ID = "V_1"
V_1 = onto.ProMoVar( onto_ID )
V_1.label = label
V_1.network = network
V_1.variable_type = variable_type
V_1.comment = doc

units = variables[1]["units"].asList()
V_1.time = [ units[0] ]
V_1.length = [ units[1] ]
V_1.amount = [ units[2] ]
V_1.mass = [ units[3] ]
V_1.temperature = [ units[4] ]
V_1.current = [ units[5] ]
V_1.light = [ units[6] ]

# 3
label = variables[3]["label"]
network = variables[3]["network"]
variable_type = variables[3]["type"]
label = variables[3]["label"]
doc = variables[3]["doc"]
onto_ID = "V_3"
V_3 = onto.ProMoVar( onto_ID )
V_3.label = label
V_3.network = network
V_3.variable_type = variable_type
V_3.comment = doc

units = variables[3]["units"].asList()
V_3.time = [ units[0] ]
V_3.length = [ units[1] ]
V_3.amount = [ units[2] ]
V_3.mass = [ units[3] ]
V_3.temperature = [ units[4] ]
V_3.current = [ units[5] ]
V_3.light = [ units[6] ]

# 4
label = variables[4]["label"]
network = variables[4]["network"]
variable_type = variables[4]["type"]
label = variables[4]["label"]
doc = variables[4]["doc"]
onto_ID = "V_4"
V_4 = onto.ProMoVar( onto_ID )
V_4.label = label
V_4.network = network
V_4.variable_type = variable_type
V_4.comment = doc

units = variables[4]["units"].asList()
V_4.time = [ units[0] ]
V_4.length = [ units[1] ]
V_4.amount = [ units[2] ]
V_4.mass = [ units[3] ]
V_4.temperature = [ units[4] ]
V_4.current = [ units[5] ]
V_4.light = [ units[6] ]

# 5
label = variables[5]["label"]
network = variables[5]["network"]
variable_type = variables[5]["type"]
label = variables[5]["label"]
doc = variables[5]["doc"]
onto_ID = "V_5"
V_5 = onto.ProMoVar( onto_ID )
V_5.label = label
V_5.network = network
V_5.variable_type = variable_type
V_5.comment = doc

units = variables[5]["units"].asList()
V_5.time = [ units[0] ]
V_5.length = [ units[1] ]
V_5.amount = [ units[2] ]
V_5.mass = [ units[3] ]
V_5.temperature = [ units[4] ]
V_5.current = [ units[5] ]
V_5.light = [ units[6] ]

# 6
label = variables[6]["label"]
network = variables[6]["network"]
variable_type = variables[6]["type"]
label = variables[6]["label"]
doc = variables[6]["doc"]
onto_ID = "V_6"
V_6 = onto.ProMoVar( onto_ID )
V_6.label = label
V_6.network = network
V_6.variable_type = variable_type
V_6.comment = doc

units = variables[6]["units"].asList()
V_6.time = [ units[0] ]
V_6.length = [ units[1] ]
V_6.amount = [ units[2] ]
V_6.mass = [ units[3] ]
V_6.temperature = [ units[4] ]
V_6.current = [ units[5] ]
V_6.light = [ units[6] ]

# 7
label = variables[7]["label"]
network = variables[7]["network"]
variable_type = variables[7]["type"]
label = variables[7]["label"]
doc = variables[7]["doc"]
onto_ID = "V_7"
V_7 = onto.ProMoVar( onto_ID )
V_7.label = label
V_7.network = network
V_7.variable_type = variable_type
V_7.comment = doc

units = variables[7]["units"].asList()
V_7.time = [ units[0] ]
V_7.length = [ units[1] ]
V_7.amount = [ units[2] ]
V_7.mass = [ units[3] ]
V_7.temperature = [ units[4] ]
V_7.current = [ units[5] ]
V_7.light = [ units[6] ]

# 8
label = variables[8]["label"]
network = variables[8]["network"]
variable_type = variables[8]["type"]
label = variables[8]["label"]
doc = variables[8]["doc"]
onto_ID = "V_8"
V_8 = onto.ProMoVar( onto_ID )
V_8.label = label
V_8.network = network
V_8.variable_type = variable_type
V_8.comment = doc

units = variables[8]["units"].asList()
V_8.time = [ units[0] ]
V_8.length = [ units[1] ]
V_8.amount = [ units[2] ]
V_8.mass = [ units[3] ]
V_8.temperature = [ units[4] ]
V_8.current = [ units[5] ]
V_8.light = [ units[6] ]

# 9
label = variables[9]["label"]
network = variables[9]["network"]
variable_type = variables[9]["type"]
label = variables[9]["label"]
doc = variables[9]["doc"]
onto_ID = "V_9"
V_9 = onto.ProMoVar( onto_ID )
V_9.label = label
V_9.network = network
V_9.variable_type = variable_type
V_9.comment = doc

units = variables[9]["units"].asList()
V_9.time = [ units[0] ]
V_9.length = [ units[1] ]
V_9.amount = [ units[2] ]
V_9.mass = [ units[3] ]
V_9.temperature = [ units[4] ]
V_9.current = [ units[5] ]
V_9.light = [ units[6] ]

# 10
label = variables[10]["label"]
network = variables[10]["network"]
variable_type = variables[10]["type"]
label = variables[10]["label"]
doc = variables[10]["doc"]
onto_ID = "V_10"
V_10 = onto.ProMoVar( onto_ID )
V_10.label = label
V_10.network = network
V_10.variable_type = variable_type
V_10.comment = doc

units = variables[10]["units"].asList()
V_10.time = [ units[0] ]
V_10.length = [ units[1] ]
V_10.amount = [ units[2] ]
V_10.mass = [ units[3] ]
V_10.temperature = [ units[4] ]
V_10.current = [ units[5] ]
V_10.light = [ units[6] ]

# 11
label = variables[11]["label"]
network = variables[11]["network"]
variable_type = variables[11]["type"]
label = variables[11]["label"]
doc = variables[11]["doc"]
onto_ID = "V_11"
V_11 = onto.ProMoVar( onto_ID )
V_11.label = label
V_11.network = network
V_11.variable_type = variable_type
V_11.comment = doc

units = variables[11]["units"].asList()
V_11.time = [ units[0] ]
V_11.length = [ units[1] ]
V_11.amount = [ units[2] ]
V_11.mass = [ units[3] ]
V_11.temperature = [ units[4] ]
V_11.current = [ units[5] ]
V_11.light = [ units[6] ]

# 12
label = variables[12]["label"]
network = variables[12]["network"]
variable_type = variables[12]["type"]
label = variables[12]["label"]
doc = variables[12]["doc"]
onto_ID = "V_12"
V_12 = onto.ProMoVar( onto_ID )
V_12.label = label
V_12.network = network
V_12.variable_type = variable_type
V_12.comment = doc

units = variables[12]["units"].asList()
V_12.time = [ units[0] ]
V_12.length = [ units[1] ]
V_12.amount = [ units[2] ]
V_12.mass = [ units[3] ]
V_12.temperature = [ units[4] ]
V_12.current = [ units[5] ]
V_12.light = [ units[6] ]

# 13
label = variables[13]["label"]
network = variables[13]["network"]
variable_type = variables[13]["type"]
label = variables[13]["label"]
doc = variables[13]["doc"]
onto_ID = "V_13"
V_13 = onto.ProMoVar( onto_ID )
V_13.label = label
V_13.network = network
V_13.variable_type = variable_type
V_13.comment = doc

units = variables[13]["units"].asList()
V_13.time = [ units[0] ]
V_13.length = [ units[1] ]
V_13.amount = [ units[2] ]
V_13.mass = [ units[3] ]
V_13.temperature = [ units[4] ]
V_13.current = [ units[5] ]
V_13.light = [ units[6] ]

# 14
label = variables[14]["label"]
network = variables[14]["network"]
variable_type = variables[14]["type"]
label = variables[14]["label"]
doc = variables[14]["doc"]
onto_ID = "V_14"
V_14 = onto.ProMoVar( onto_ID )
V_14.label = label
V_14.network = network
V_14.variable_type = variable_type
V_14.comment = doc

units = variables[14]["units"].asList()
V_14.time = [ units[0] ]
V_14.length = [ units[1] ]
V_14.amount = [ units[2] ]
V_14.mass = [ units[3] ]
V_14.temperature = [ units[4] ]
V_14.current = [ units[5] ]
V_14.light = [ units[6] ]

# 15
label = variables[15]["label"]
network = variables[15]["network"]
variable_type = variables[15]["type"]
label = variables[15]["label"]
doc = variables[15]["doc"]
onto_ID = "V_15"
V_15 = onto.ProMoVar( onto_ID )
V_15.label = label
V_15.network = network
V_15.variable_type = variable_type
V_15.comment = doc

units = variables[15]["units"].asList()
V_15.time = [ units[0] ]
V_15.length = [ units[1] ]
V_15.amount = [ units[2] ]
V_15.mass = [ units[3] ]
V_15.temperature = [ units[4] ]
V_15.current = [ units[5] ]
V_15.light = [ units[6] ]

# 16
label = variables[16]["label"]
network = variables[16]["network"]
variable_type = variables[16]["type"]
label = variables[16]["label"]
doc = variables[16]["doc"]
onto_ID = "V_16"
V_16 = onto.ProMoVar( onto_ID )
V_16.label = label
V_16.network = network
V_16.variable_type = variable_type
V_16.comment = doc

units = variables[16]["units"].asList()
V_16.time = [ units[0] ]
V_16.length = [ units[1] ]
V_16.amount = [ units[2] ]
V_16.mass = [ units[3] ]
V_16.temperature = [ units[4] ]
V_16.current = [ units[5] ]
V_16.light = [ units[6] ]

# 17
label = variables[17]["label"]
network = variables[17]["network"]
variable_type = variables[17]["type"]
label = variables[17]["label"]
doc = variables[17]["doc"]
onto_ID = "V_17"
V_17 = onto.ProMoVar( onto_ID )
V_17.label = label
V_17.network = network
V_17.variable_type = variable_type
V_17.comment = doc

units = variables[17]["units"].asList()
V_17.time = [ units[0] ]
V_17.length = [ units[1] ]
V_17.amount = [ units[2] ]
V_17.mass = [ units[3] ]
V_17.temperature = [ units[4] ]
V_17.current = [ units[5] ]
V_17.light = [ units[6] ]

# 18
label = variables[18]["label"]
network = variables[18]["network"]
variable_type = variables[18]["type"]
label = variables[18]["label"]
doc = variables[18]["doc"]
onto_ID = "V_18"
V_18 = onto.ProMoVar( onto_ID )
V_18.label = label
V_18.network = network
V_18.variable_type = variable_type
V_18.comment = doc

units = variables[18]["units"].asList()
V_18.time = [ units[0] ]
V_18.length = [ units[1] ]
V_18.amount = [ units[2] ]
V_18.mass = [ units[3] ]
V_18.temperature = [ units[4] ]
V_18.current = [ units[5] ]
V_18.light = [ units[6] ]

# 19
label = variables[19]["label"]
network = variables[19]["network"]
variable_type = variables[19]["type"]
label = variables[19]["label"]
doc = variables[19]["doc"]
onto_ID = "V_19"
V_19 = onto.ProMoVar( onto_ID )
V_19.label = label
V_19.network = network
V_19.variable_type = variable_type
V_19.comment = doc

units = variables[19]["units"].asList()
V_19.time = [ units[0] ]
V_19.length = [ units[1] ]
V_19.amount = [ units[2] ]
V_19.mass = [ units[3] ]
V_19.temperature = [ units[4] ]
V_19.current = [ units[5] ]
V_19.light = [ units[6] ]

# 20
label = variables[20]["label"]
network = variables[20]["network"]
variable_type = variables[20]["type"]
label = variables[20]["label"]
doc = variables[20]["doc"]
onto_ID = "V_20"
V_20 = onto.ProMoVar( onto_ID )
V_20.label = label
V_20.network = network
V_20.variable_type = variable_type
V_20.comment = doc

units = variables[20]["units"].asList()
V_20.time = [ units[0] ]
V_20.length = [ units[1] ]
V_20.amount = [ units[2] ]
V_20.mass = [ units[3] ]
V_20.temperature = [ units[4] ]
V_20.current = [ units[5] ]
V_20.light = [ units[6] ]

# 21
label = variables[21]["label"]
network = variables[21]["network"]
variable_type = variables[21]["type"]
label = variables[21]["label"]
doc = variables[21]["doc"]
onto_ID = "V_21"
V_21 = onto.ProMoVar( onto_ID )
V_21.label = label
V_21.network = network
V_21.variable_type = variable_type
V_21.comment = doc

units = variables[21]["units"].asList()
V_21.time = [ units[0] ]
V_21.length = [ units[1] ]
V_21.amount = [ units[2] ]
V_21.mass = [ units[3] ]
V_21.temperature = [ units[4] ]
V_21.current = [ units[5] ]
V_21.light = [ units[6] ]

# 22
label = variables[22]["label"]
network = variables[22]["network"]
variable_type = variables[22]["type"]
label = variables[22]["label"]
doc = variables[22]["doc"]
onto_ID = "V_22"
V_22 = onto.ProMoVar( onto_ID )
V_22.label = label
V_22.network = network
V_22.variable_type = variable_type
V_22.comment = doc

units = variables[22]["units"].asList()
V_22.time = [ units[0] ]
V_22.length = [ units[1] ]
V_22.amount = [ units[2] ]
V_22.mass = [ units[3] ]
V_22.temperature = [ units[4] ]
V_22.current = [ units[5] ]
V_22.light = [ units[6] ]

# 23
label = variables[23]["label"]
network = variables[23]["network"]
variable_type = variables[23]["type"]
label = variables[23]["label"]
doc = variables[23]["doc"]
onto_ID = "V_23"
V_23 = onto.ProMoVar( onto_ID )
V_23.label = label
V_23.network = network
V_23.variable_type = variable_type
V_23.comment = doc

units = variables[23]["units"].asList()
V_23.time = [ units[0] ]
V_23.length = [ units[1] ]
V_23.amount = [ units[2] ]
V_23.mass = [ units[3] ]
V_23.temperature = [ units[4] ]
V_23.current = [ units[5] ]
V_23.light = [ units[6] ]

# 24
label = variables[24]["label"]
network = variables[24]["network"]
variable_type = variables[24]["type"]
label = variables[24]["label"]
doc = variables[24]["doc"]
onto_ID = "V_24"
V_24 = onto.ProMoVar( onto_ID )
V_24.label = label
V_24.network = network
V_24.variable_type = variable_type
V_24.comment = doc

units = variables[24]["units"].asList()
V_24.time = [ units[0] ]
V_24.length = [ units[1] ]
V_24.amount = [ units[2] ]
V_24.mass = [ units[3] ]
V_24.temperature = [ units[4] ]
V_24.current = [ units[5] ]
V_24.light = [ units[6] ]

# 25
label = variables[25]["label"]
network = variables[25]["network"]
variable_type = variables[25]["type"]
label = variables[25]["label"]
doc = variables[25]["doc"]
onto_ID = "V_25"
V_25 = onto.ProMoVar( onto_ID )
V_25.label = label
V_25.network = network
V_25.variable_type = variable_type
V_25.comment = doc

units = variables[25]["units"].asList()
V_25.time = [ units[0] ]
V_25.length = [ units[1] ]
V_25.amount = [ units[2] ]
V_25.mass = [ units[3] ]
V_25.temperature = [ units[4] ]
V_25.current = [ units[5] ]
V_25.light = [ units[6] ]

# 26
label = variables[26]["label"]
network = variables[26]["network"]
variable_type = variables[26]["type"]
label = variables[26]["label"]
doc = variables[26]["doc"]
onto_ID = "V_26"
V_26 = onto.ProMoVar( onto_ID )
V_26.label = label
V_26.network = network
V_26.variable_type = variable_type
V_26.comment = doc

units = variables[26]["units"].asList()
V_26.time = [ units[0] ]
V_26.length = [ units[1] ]
V_26.amount = [ units[2] ]
V_26.mass = [ units[3] ]
V_26.temperature = [ units[4] ]
V_26.current = [ units[5] ]
V_26.light = [ units[6] ]

# 27
label = variables[27]["label"]
network = variables[27]["network"]
variable_type = variables[27]["type"]
label = variables[27]["label"]
doc = variables[27]["doc"]
onto_ID = "V_27"
V_27 = onto.ProMoVar( onto_ID )
V_27.label = label
V_27.network = network
V_27.variable_type = variable_type
V_27.comment = doc

units = variables[27]["units"].asList()
V_27.time = [ units[0] ]
V_27.length = [ units[1] ]
V_27.amount = [ units[2] ]
V_27.mass = [ units[3] ]
V_27.temperature = [ units[4] ]
V_27.current = [ units[5] ]
V_27.light = [ units[6] ]

# 28
label = variables[28]["label"]
network = variables[28]["network"]
variable_type = variables[28]["type"]
label = variables[28]["label"]
doc = variables[28]["doc"]
onto_ID = "V_28"
V_28 = onto.ProMoVar( onto_ID )
V_28.label = label
V_28.network = network
V_28.variable_type = variable_type
V_28.comment = doc

units = variables[28]["units"].asList()
V_28.time = [ units[0] ]
V_28.length = [ units[1] ]
V_28.amount = [ units[2] ]
V_28.mass = [ units[3] ]
V_28.temperature = [ units[4] ]
V_28.current = [ units[5] ]
V_28.light = [ units[6] ]

# 29
label = variables[29]["label"]
network = variables[29]["network"]
variable_type = variables[29]["type"]
label = variables[29]["label"]
doc = variables[29]["doc"]
onto_ID = "V_29"
V_29 = onto.ProMoVar( onto_ID )
V_29.label = label
V_29.network = network
V_29.variable_type = variable_type
V_29.comment = doc

units = variables[29]["units"].asList()
V_29.time = [ units[0] ]
V_29.length = [ units[1] ]
V_29.amount = [ units[2] ]
V_29.mass = [ units[3] ]
V_29.temperature = [ units[4] ]
V_29.current = [ units[5] ]
V_29.light = [ units[6] ]

# 30
label = variables[30]["label"]
network = variables[30]["network"]
variable_type = variables[30]["type"]
label = variables[30]["label"]
doc = variables[30]["doc"]
onto_ID = "V_30"
V_30 = onto.ProMoVar( onto_ID )
V_30.label = label
V_30.network = network
V_30.variable_type = variable_type
V_30.comment = doc

units = variables[30]["units"].asList()
V_30.time = [ units[0] ]
V_30.length = [ units[1] ]
V_30.amount = [ units[2] ]
V_30.mass = [ units[3] ]
V_30.temperature = [ units[4] ]
V_30.current = [ units[5] ]
V_30.light = [ units[6] ]

# 31
label = variables[31]["label"]
network = variables[31]["network"]
variable_type = variables[31]["type"]
label = variables[31]["label"]
doc = variables[31]["doc"]
onto_ID = "V_31"
V_31 = onto.ProMoVar( onto_ID )
V_31.label = label
V_31.network = network
V_31.variable_type = variable_type
V_31.comment = doc

units = variables[31]["units"].asList()
V_31.time = [ units[0] ]
V_31.length = [ units[1] ]
V_31.amount = [ units[2] ]
V_31.mass = [ units[3] ]
V_31.temperature = [ units[4] ]
V_31.current = [ units[5] ]
V_31.light = [ units[6] ]

# 32
label = variables[32]["label"]
network = variables[32]["network"]
variable_type = variables[32]["type"]
label = variables[32]["label"]
doc = variables[32]["doc"]
onto_ID = "V_32"
V_32 = onto.ProMoVar( onto_ID )
V_32.label = label
V_32.network = network
V_32.variable_type = variable_type
V_32.comment = doc

units = variables[32]["units"].asList()
V_32.time = [ units[0] ]
V_32.length = [ units[1] ]
V_32.amount = [ units[2] ]
V_32.mass = [ units[3] ]
V_32.temperature = [ units[4] ]
V_32.current = [ units[5] ]
V_32.light = [ units[6] ]

# 33
label = variables[33]["label"]
network = variables[33]["network"]
variable_type = variables[33]["type"]
label = variables[33]["label"]
doc = variables[33]["doc"]
onto_ID = "V_33"
V_33 = onto.ProMoVar( onto_ID )
V_33.label = label
V_33.network = network
V_33.variable_type = variable_type
V_33.comment = doc

units = variables[33]["units"].asList()
V_33.time = [ units[0] ]
V_33.length = [ units[1] ]
V_33.amount = [ units[2] ]
V_33.mass = [ units[3] ]
V_33.temperature = [ units[4] ]
V_33.current = [ units[5] ]
V_33.light = [ units[6] ]

# 34
label = variables[34]["label"]
network = variables[34]["network"]
variable_type = variables[34]["type"]
label = variables[34]["label"]
doc = variables[34]["doc"]
onto_ID = "V_34"
V_34 = onto.ProMoVar( onto_ID )
V_34.label = label
V_34.network = network
V_34.variable_type = variable_type
V_34.comment = doc

units = variables[34]["units"].asList()
V_34.time = [ units[0] ]
V_34.length = [ units[1] ]
V_34.amount = [ units[2] ]
V_34.mass = [ units[3] ]
V_34.temperature = [ units[4] ]
V_34.current = [ units[5] ]
V_34.light = [ units[6] ]

# 35
label = variables[35]["label"]
network = variables[35]["network"]
variable_type = variables[35]["type"]
label = variables[35]["label"]
doc = variables[35]["doc"]
onto_ID = "V_35"
V_35 = onto.ProMoVar( onto_ID )
V_35.label = label
V_35.network = network
V_35.variable_type = variable_type
V_35.comment = doc

units = variables[35]["units"].asList()
V_35.time = [ units[0] ]
V_35.length = [ units[1] ]
V_35.amount = [ units[2] ]
V_35.mass = [ units[3] ]
V_35.temperature = [ units[4] ]
V_35.current = [ units[5] ]
V_35.light = [ units[6] ]

# 36
label = variables[36]["label"]
network = variables[36]["network"]
variable_type = variables[36]["type"]
label = variables[36]["label"]
doc = variables[36]["doc"]
onto_ID = "V_36"
V_36 = onto.ProMoVar( onto_ID )
V_36.label = label
V_36.network = network
V_36.variable_type = variable_type
V_36.comment = doc

units = variables[36]["units"].asList()
V_36.time = [ units[0] ]
V_36.length = [ units[1] ]
V_36.amount = [ units[2] ]
V_36.mass = [ units[3] ]
V_36.temperature = [ units[4] ]
V_36.current = [ units[5] ]
V_36.light = [ units[6] ]

# 50
label = variables[50]["label"]
network = variables[50]["network"]
variable_type = variables[50]["type"]
label = variables[50]["label"]
doc = variables[50]["doc"]
onto_ID = "V_50"
V_50 = onto.ProMoVar( onto_ID )
V_50.label = label
V_50.network = network
V_50.variable_type = variable_type
V_50.comment = doc

units = variables[50]["units"].asList()
V_50.time = [ units[0] ]
V_50.length = [ units[1] ]
V_50.amount = [ units[2] ]
V_50.mass = [ units[3] ]
V_50.temperature = [ units[4] ]
V_50.current = [ units[5] ]
V_50.light = [ units[6] ]

# 51
label = variables[51]["label"]
network = variables[51]["network"]
variable_type = variables[51]["type"]
label = variables[51]["label"]
doc = variables[51]["doc"]
onto_ID = "V_51"
V_51 = onto.ProMoVar( onto_ID )
V_51.label = label
V_51.network = network
V_51.variable_type = variable_type
V_51.comment = doc

units = variables[51]["units"].asList()
V_51.time = [ units[0] ]
V_51.length = [ units[1] ]
V_51.amount = [ units[2] ]
V_51.mass = [ units[3] ]
V_51.temperature = [ units[4] ]
V_51.current = [ units[5] ]
V_51.light = [ units[6] ]

# 52
label = variables[52]["label"]
network = variables[52]["network"]
variable_type = variables[52]["type"]
label = variables[52]["label"]
doc = variables[52]["doc"]
onto_ID = "V_52"
V_52 = onto.ProMoVar( onto_ID )
V_52.label = label
V_52.network = network
V_52.variable_type = variable_type
V_52.comment = doc

units = variables[52]["units"].asList()
V_52.time = [ units[0] ]
V_52.length = [ units[1] ]
V_52.amount = [ units[2] ]
V_52.mass = [ units[3] ]
V_52.temperature = [ units[4] ]
V_52.current = [ units[5] ]
V_52.light = [ units[6] ]

# 53
label = variables[53]["label"]
network = variables[53]["network"]
variable_type = variables[53]["type"]
label = variables[53]["label"]
doc = variables[53]["doc"]
onto_ID = "V_53"
V_53 = onto.ProMoVar( onto_ID )
V_53.label = label
V_53.network = network
V_53.variable_type = variable_type
V_53.comment = doc

units = variables[53]["units"].asList()
V_53.time = [ units[0] ]
V_53.length = [ units[1] ]
V_53.amount = [ units[2] ]
V_53.mass = [ units[3] ]
V_53.temperature = [ units[4] ]
V_53.current = [ units[5] ]
V_53.light = [ units[6] ]

# 55
label = variables[55]["label"]
network = variables[55]["network"]
variable_type = variables[55]["type"]
label = variables[55]["label"]
doc = variables[55]["doc"]
onto_ID = "V_55"
V_55 = onto.ProMoVar( onto_ID )
V_55.label = label
V_55.network = network
V_55.variable_type = variable_type
V_55.comment = doc

units = variables[55]["units"].asList()
V_55.time = [ units[0] ]
V_55.length = [ units[1] ]
V_55.amount = [ units[2] ]
V_55.mass = [ units[3] ]
V_55.temperature = [ units[4] ]
V_55.current = [ units[5] ]
V_55.light = [ units[6] ]

# 56
label = variables[56]["label"]
network = variables[56]["network"]
variable_type = variables[56]["type"]
label = variables[56]["label"]
doc = variables[56]["doc"]
onto_ID = "V_56"
V_56 = onto.ProMoVar( onto_ID )
V_56.label = label
V_56.network = network
V_56.variable_type = variable_type
V_56.comment = doc

units = variables[56]["units"].asList()
V_56.time = [ units[0] ]
V_56.length = [ units[1] ]
V_56.amount = [ units[2] ]
V_56.mass = [ units[3] ]
V_56.temperature = [ units[4] ]
V_56.current = [ units[5] ]
V_56.light = [ units[6] ]

# 57
label = variables[57]["label"]
network = variables[57]["network"]
variable_type = variables[57]["type"]
label = variables[57]["label"]
doc = variables[57]["doc"]
onto_ID = "V_57"
V_57 = onto.ProMoVar( onto_ID )
V_57.label = label
V_57.network = network
V_57.variable_type = variable_type
V_57.comment = doc

units = variables[57]["units"].asList()
V_57.time = [ units[0] ]
V_57.length = [ units[1] ]
V_57.amount = [ units[2] ]
V_57.mass = [ units[3] ]
V_57.temperature = [ units[4] ]
V_57.current = [ units[5] ]
V_57.light = [ units[6] ]

# 58
label = variables[58]["label"]
network = variables[58]["network"]
variable_type = variables[58]["type"]
label = variables[58]["label"]
doc = variables[58]["doc"]
onto_ID = "V_58"
V_58 = onto.ProMoVar( onto_ID )
V_58.label = label
V_58.network = network
V_58.variable_type = variable_type
V_58.comment = doc

units = variables[58]["units"].asList()
V_58.time = [ units[0] ]
V_58.length = [ units[1] ]
V_58.amount = [ units[2] ]
V_58.mass = [ units[3] ]
V_58.temperature = [ units[4] ]
V_58.current = [ units[5] ]
V_58.light = [ units[6] ]

# 59
label = variables[59]["label"]
network = variables[59]["network"]
variable_type = variables[59]["type"]
label = variables[59]["label"]
doc = variables[59]["doc"]
onto_ID = "V_59"
V_59 = onto.ProMoVar( onto_ID )
V_59.label = label
V_59.network = network
V_59.variable_type = variable_type
V_59.comment = doc

units = variables[59]["units"].asList()
V_59.time = [ units[0] ]
V_59.length = [ units[1] ]
V_59.amount = [ units[2] ]
V_59.mass = [ units[3] ]
V_59.temperature = [ units[4] ]
V_59.current = [ units[5] ]
V_59.light = [ units[6] ]

# 60
label = variables[60]["label"]
network = variables[60]["network"]
variable_type = variables[60]["type"]
label = variables[60]["label"]
doc = variables[60]["doc"]
onto_ID = "V_60"
V_60 = onto.ProMoVar( onto_ID )
V_60.label = label
V_60.network = network
V_60.variable_type = variable_type
V_60.comment = doc

units = variables[60]["units"].asList()
V_60.time = [ units[0] ]
V_60.length = [ units[1] ]
V_60.amount = [ units[2] ]
V_60.mass = [ units[3] ]
V_60.temperature = [ units[4] ]
V_60.current = [ units[5] ]
V_60.light = [ units[6] ]

# 61
label = variables[61]["label"]
network = variables[61]["network"]
variable_type = variables[61]["type"]
label = variables[61]["label"]
doc = variables[61]["doc"]
onto_ID = "V_61"
V_61 = onto.ProMoVar( onto_ID )
V_61.label = label
V_61.network = network
V_61.variable_type = variable_type
V_61.comment = doc

units = variables[61]["units"].asList()
V_61.time = [ units[0] ]
V_61.length = [ units[1] ]
V_61.amount = [ units[2] ]
V_61.mass = [ units[3] ]
V_61.temperature = [ units[4] ]
V_61.current = [ units[5] ]
V_61.light = [ units[6] ]

# 62
label = variables[62]["label"]
network = variables[62]["network"]
variable_type = variables[62]["type"]
label = variables[62]["label"]
doc = variables[62]["doc"]
onto_ID = "V_62"
V_62 = onto.ProMoVar( onto_ID )
V_62.label = label
V_62.network = network
V_62.variable_type = variable_type
V_62.comment = doc

units = variables[62]["units"].asList()
V_62.time = [ units[0] ]
V_62.length = [ units[1] ]
V_62.amount = [ units[2] ]
V_62.mass = [ units[3] ]
V_62.temperature = [ units[4] ]
V_62.current = [ units[5] ]
V_62.light = [ units[6] ]

# 63
label = variables[63]["label"]
network = variables[63]["network"]
variable_type = variables[63]["type"]
label = variables[63]["label"]
doc = variables[63]["doc"]
onto_ID = "V_63"
V_63 = onto.ProMoVar( onto_ID )
V_63.label = label
V_63.network = network
V_63.variable_type = variable_type
V_63.comment = doc

units = variables[63]["units"].asList()
V_63.time = [ units[0] ]
V_63.length = [ units[1] ]
V_63.amount = [ units[2] ]
V_63.mass = [ units[3] ]
V_63.temperature = [ units[4] ]
V_63.current = [ units[5] ]
V_63.light = [ units[6] ]

# 64
label = variables[64]["label"]
network = variables[64]["network"]
variable_type = variables[64]["type"]
label = variables[64]["label"]
doc = variables[64]["doc"]
onto_ID = "V_64"
V_64 = onto.ProMoVar( onto_ID )
V_64.label = label
V_64.network = network
V_64.variable_type = variable_type
V_64.comment = doc

units = variables[64]["units"].asList()
V_64.time = [ units[0] ]
V_64.length = [ units[1] ]
V_64.amount = [ units[2] ]
V_64.mass = [ units[3] ]
V_64.temperature = [ units[4] ]
V_64.current = [ units[5] ]
V_64.light = [ units[6] ]

# 65
label = variables[65]["label"]
network = variables[65]["network"]
variable_type = variables[65]["type"]
label = variables[65]["label"]
doc = variables[65]["doc"]
onto_ID = "V_65"
V_65 = onto.ProMoVar( onto_ID )
V_65.label = label
V_65.network = network
V_65.variable_type = variable_type
V_65.comment = doc

units = variables[65]["units"].asList()
V_65.time = [ units[0] ]
V_65.length = [ units[1] ]
V_65.amount = [ units[2] ]
V_65.mass = [ units[3] ]
V_65.temperature = [ units[4] ]
V_65.current = [ units[5] ]
V_65.light = [ units[6] ]

# 66
label = variables[66]["label"]
network = variables[66]["network"]
variable_type = variables[66]["type"]
label = variables[66]["label"]
doc = variables[66]["doc"]
onto_ID = "V_66"
V_66 = onto.ProMoVar( onto_ID )
V_66.label = label
V_66.network = network
V_66.variable_type = variable_type
V_66.comment = doc

units = variables[66]["units"].asList()
V_66.time = [ units[0] ]
V_66.length = [ units[1] ]
V_66.amount = [ units[2] ]
V_66.mass = [ units[3] ]
V_66.temperature = [ units[4] ]
V_66.current = [ units[5] ]
V_66.light = [ units[6] ]

# 67
label = variables[67]["label"]
network = variables[67]["network"]
variable_type = variables[67]["type"]
label = variables[67]["label"]
doc = variables[67]["doc"]
onto_ID = "V_67"
V_67 = onto.ProMoVar( onto_ID )
V_67.label = label
V_67.network = network
V_67.variable_type = variable_type
V_67.comment = doc

units = variables[67]["units"].asList()
V_67.time = [ units[0] ]
V_67.length = [ units[1] ]
V_67.amount = [ units[2] ]
V_67.mass = [ units[3] ]
V_67.temperature = [ units[4] ]
V_67.current = [ units[5] ]
V_67.light = [ units[6] ]

# 68
label = variables[68]["label"]
network = variables[68]["network"]
variable_type = variables[68]["type"]
label = variables[68]["label"]
doc = variables[68]["doc"]
onto_ID = "V_68"
V_68 = onto.ProMoVar( onto_ID )
V_68.label = label
V_68.network = network
V_68.variable_type = variable_type
V_68.comment = doc

units = variables[68]["units"].asList()
V_68.time = [ units[0] ]
V_68.length = [ units[1] ]
V_68.amount = [ units[2] ]
V_68.mass = [ units[3] ]
V_68.temperature = [ units[4] ]
V_68.current = [ units[5] ]
V_68.light = [ units[6] ]

# 69
label = variables[69]["label"]
network = variables[69]["network"]
variable_type = variables[69]["type"]
label = variables[69]["label"]
doc = variables[69]["doc"]
onto_ID = "V_69"
V_69 = onto.ProMoVar( onto_ID )
V_69.label = label
V_69.network = network
V_69.variable_type = variable_type
V_69.comment = doc

units = variables[69]["units"].asList()
V_69.time = [ units[0] ]
V_69.length = [ units[1] ]
V_69.amount = [ units[2] ]
V_69.mass = [ units[3] ]
V_69.temperature = [ units[4] ]
V_69.current = [ units[5] ]
V_69.light = [ units[6] ]

# 70
label = variables[70]["label"]
network = variables[70]["network"]
variable_type = variables[70]["type"]
label = variables[70]["label"]
doc = variables[70]["doc"]
onto_ID = "V_70"
V_70 = onto.ProMoVar( onto_ID )
V_70.label = label
V_70.network = network
V_70.variable_type = variable_type
V_70.comment = doc

units = variables[70]["units"].asList()
V_70.time = [ units[0] ]
V_70.length = [ units[1] ]
V_70.amount = [ units[2] ]
V_70.mass = [ units[3] ]
V_70.temperature = [ units[4] ]
V_70.current = [ units[5] ]
V_70.light = [ units[6] ]

# 71
label = variables[71]["label"]
network = variables[71]["network"]
variable_type = variables[71]["type"]
label = variables[71]["label"]
doc = variables[71]["doc"]
onto_ID = "V_71"
V_71 = onto.ProMoVar( onto_ID )
V_71.label = label
V_71.network = network
V_71.variable_type = variable_type
V_71.comment = doc

units = variables[71]["units"].asList()
V_71.time = [ units[0] ]
V_71.length = [ units[1] ]
V_71.amount = [ units[2] ]
V_71.mass = [ units[3] ]
V_71.temperature = [ units[4] ]
V_71.current = [ units[5] ]
V_71.light = [ units[6] ]

# 72
label = variables[72]["label"]
network = variables[72]["network"]
variable_type = variables[72]["type"]
label = variables[72]["label"]
doc = variables[72]["doc"]
onto_ID = "V_72"
V_72 = onto.ProMoVar( onto_ID )
V_72.label = label
V_72.network = network
V_72.variable_type = variable_type
V_72.comment = doc

units = variables[72]["units"].asList()
V_72.time = [ units[0] ]
V_72.length = [ units[1] ]
V_72.amount = [ units[2] ]
V_72.mass = [ units[3] ]
V_72.temperature = [ units[4] ]
V_72.current = [ units[5] ]
V_72.light = [ units[6] ]

# 73
label = variables[73]["label"]
network = variables[73]["network"]
variable_type = variables[73]["type"]
label = variables[73]["label"]
doc = variables[73]["doc"]
onto_ID = "V_73"
V_73 = onto.ProMoVar( onto_ID )
V_73.label = label
V_73.network = network
V_73.variable_type = variable_type
V_73.comment = doc

units = variables[73]["units"].asList()
V_73.time = [ units[0] ]
V_73.length = [ units[1] ]
V_73.amount = [ units[2] ]
V_73.mass = [ units[3] ]
V_73.temperature = [ units[4] ]
V_73.current = [ units[5] ]
V_73.light = [ units[6] ]

# 74
label = variables[74]["label"]
network = variables[74]["network"]
variable_type = variables[74]["type"]
label = variables[74]["label"]
doc = variables[74]["doc"]
onto_ID = "V_74"
V_74 = onto.ProMoVar( onto_ID )
V_74.label = label
V_74.network = network
V_74.variable_type = variable_type
V_74.comment = doc

units = variables[74]["units"].asList()
V_74.time = [ units[0] ]
V_74.length = [ units[1] ]
V_74.amount = [ units[2] ]
V_74.mass = [ units[3] ]
V_74.temperature = [ units[4] ]
V_74.current = [ units[5] ]
V_74.light = [ units[6] ]

# 75
label = variables[75]["label"]
network = variables[75]["network"]
variable_type = variables[75]["type"]
label = variables[75]["label"]
doc = variables[75]["doc"]
onto_ID = "V_75"
V_75 = onto.ProMoVar( onto_ID )
V_75.label = label
V_75.network = network
V_75.variable_type = variable_type
V_75.comment = doc

units = variables[75]["units"].asList()
V_75.time = [ units[0] ]
V_75.length = [ units[1] ]
V_75.amount = [ units[2] ]
V_75.mass = [ units[3] ]
V_75.temperature = [ units[4] ]
V_75.current = [ units[5] ]
V_75.light = [ units[6] ]

# 76
label = variables[76]["label"]
network = variables[76]["network"]
variable_type = variables[76]["type"]
label = variables[76]["label"]
doc = variables[76]["doc"]
onto_ID = "V_76"
V_76 = onto.ProMoVar( onto_ID )
V_76.label = label
V_76.network = network
V_76.variable_type = variable_type
V_76.comment = doc

units = variables[76]["units"].asList()
V_76.time = [ units[0] ]
V_76.length = [ units[1] ]
V_76.amount = [ units[2] ]
V_76.mass = [ units[3] ]
V_76.temperature = [ units[4] ]
V_76.current = [ units[5] ]
V_76.light = [ units[6] ]

# 77
label = variables[77]["label"]
network = variables[77]["network"]
variable_type = variables[77]["type"]
label = variables[77]["label"]
doc = variables[77]["doc"]
onto_ID = "V_77"
V_77 = onto.ProMoVar( onto_ID )
V_77.label = label
V_77.network = network
V_77.variable_type = variable_type
V_77.comment = doc

units = variables[77]["units"].asList()
V_77.time = [ units[0] ]
V_77.length = [ units[1] ]
V_77.amount = [ units[2] ]
V_77.mass = [ units[3] ]
V_77.temperature = [ units[4] ]
V_77.current = [ units[5] ]
V_77.light = [ units[6] ]

# 78
label = variables[78]["label"]
network = variables[78]["network"]
variable_type = variables[78]["type"]
label = variables[78]["label"]
doc = variables[78]["doc"]
onto_ID = "V_78"
V_78 = onto.ProMoVar( onto_ID )
V_78.label = label
V_78.network = network
V_78.variable_type = variable_type
V_78.comment = doc

units = variables[78]["units"].asList()
V_78.time = [ units[0] ]
V_78.length = [ units[1] ]
V_78.amount = [ units[2] ]
V_78.mass = [ units[3] ]
V_78.temperature = [ units[4] ]
V_78.current = [ units[5] ]
V_78.light = [ units[6] ]

# 79
label = variables[79]["label"]
network = variables[79]["network"]
variable_type = variables[79]["type"]
label = variables[79]["label"]
doc = variables[79]["doc"]
onto_ID = "V_79"
V_79 = onto.ProMoVar( onto_ID )
V_79.label = label
V_79.network = network
V_79.variable_type = variable_type
V_79.comment = doc

units = variables[79]["units"].asList()
V_79.time = [ units[0] ]
V_79.length = [ units[1] ]
V_79.amount = [ units[2] ]
V_79.mass = [ units[3] ]
V_79.temperature = [ units[4] ]
V_79.current = [ units[5] ]
V_79.light = [ units[6] ]

# 80
label = variables[80]["label"]
network = variables[80]["network"]
variable_type = variables[80]["type"]
label = variables[80]["label"]
doc = variables[80]["doc"]
onto_ID = "V_80"
V_80 = onto.ProMoVar( onto_ID )
V_80.label = label
V_80.network = network
V_80.variable_type = variable_type
V_80.comment = doc

units = variables[80]["units"].asList()
V_80.time = [ units[0] ]
V_80.length = [ units[1] ]
V_80.amount = [ units[2] ]
V_80.mass = [ units[3] ]
V_80.temperature = [ units[4] ]
V_80.current = [ units[5] ]
V_80.light = [ units[6] ]

# 81
label = variables[81]["label"]
network = variables[81]["network"]
variable_type = variables[81]["type"]
label = variables[81]["label"]
doc = variables[81]["doc"]
onto_ID = "V_81"
V_81 = onto.ProMoVar( onto_ID )
V_81.label = label
V_81.network = network
V_81.variable_type = variable_type
V_81.comment = doc

units = variables[81]["units"].asList()
V_81.time = [ units[0] ]
V_81.length = [ units[1] ]
V_81.amount = [ units[2] ]
V_81.mass = [ units[3] ]
V_81.temperature = [ units[4] ]
V_81.current = [ units[5] ]
V_81.light = [ units[6] ]

# 82
label = variables[82]["label"]
network = variables[82]["network"]
variable_type = variables[82]["type"]
label = variables[82]["label"]
doc = variables[82]["doc"]
onto_ID = "V_82"
V_82 = onto.ProMoVar( onto_ID )
V_82.label = label
V_82.network = network
V_82.variable_type = variable_type
V_82.comment = doc

units = variables[82]["units"].asList()
V_82.time = [ units[0] ]
V_82.length = [ units[1] ]
V_82.amount = [ units[2] ]
V_82.mass = [ units[3] ]
V_82.temperature = [ units[4] ]
V_82.current = [ units[5] ]
V_82.light = [ units[6] ]

# 83
label = variables[83]["label"]
network = variables[83]["network"]
variable_type = variables[83]["type"]
label = variables[83]["label"]
doc = variables[83]["doc"]
onto_ID = "V_83"
V_83 = onto.ProMoVar( onto_ID )
V_83.label = label
V_83.network = network
V_83.variable_type = variable_type
V_83.comment = doc

units = variables[83]["units"].asList()
V_83.time = [ units[0] ]
V_83.length = [ units[1] ]
V_83.amount = [ units[2] ]
V_83.mass = [ units[3] ]
V_83.temperature = [ units[4] ]
V_83.current = [ units[5] ]
V_83.light = [ units[6] ]

# functions assignments

#1

V_1.has_function = []
#3

V_3.has_function = []
#4

V_4.has_function = []
incidence_list = []
incidence_list.append( V_3 )
incidence_list.append( V_3 )
F_ID = "F_1"
F_1 = onto.function( F_ID )
F_1.is_function_of = incidence_list
V_4.has_function.append( F_1 )
#5

V_5.has_function = []
incidence_list = []
incidence_list.append( V_3 )
incidence_list.append( V_3 )
F_ID = "F_2"
F_2 = onto.function( F_ID )
F_2.is_function_of = incidence_list
V_5.has_function.append( F_2 )
#6

V_6.has_function = []
incidence_list = []
incidence_list.append( V_1 )
incidence_list.append( V_3 )
F_ID = "F_3"
F_3 = onto.function( F_ID )
F_3.is_function_of = incidence_list
V_6.has_function.append( F_3 )
#7

V_7.has_function = []
incidence_list = []
incidence_list.append( V_1 )
incidence_list.append( V_3 )
F_ID = "F_4"
F_4 = onto.function( F_ID )
F_4.is_function_of = incidence_list
V_7.has_function.append( F_4 )
#8

V_8.has_function = []
#9

V_9.has_function = []
incidence_list = []
incidence_list.append( V_29 )
incidence_list.append( V_1 )
incidence_list.append( V_6 )
incidence_list.append( V_7 )
incidence_list.append( V_11 )
F_ID = "F_20"
F_20 = onto.function( F_ID )
F_20.is_function_of = incidence_list
V_9.has_function.append( F_20 )
#10

V_10.has_function = []
incidence_list = []
incidence_list.append( V_30 )
incidence_list.append( V_1 )
incidence_list.append( V_6 )
incidence_list.append( V_7 )
incidence_list.append( V_12 )
F_ID = "F_21"
F_21 = onto.function( F_ID )
F_21.is_function_of = incidence_list
V_10.has_function.append( F_21 )
#11

V_11.has_function = []
incidence_list = []
incidence_list.append( V_9 )
incidence_list.append( V_3 )
F_ID = "F_5"
F_5 = onto.function( F_ID )
F_5.is_function_of = incidence_list
V_11.has_function.append( F_5 )
#12

V_12.has_function = []
incidence_list = []
incidence_list.append( V_10 )
incidence_list.append( V_3 )
F_ID = "F_6"
F_6 = onto.function( F_ID )
F_6.is_function_of = incidence_list
V_12.has_function.append( F_6 )
#13

V_13.has_function = []
#14

V_14.has_function = []
#15

V_15.has_function = []
#16

V_16.has_function = []
#17

V_17.has_function = []
#18

V_18.has_function = []
#19

V_19.has_function = []
#20

V_20.has_function = []
#21

V_21.has_function = []
incidence_list = []
incidence_list.append( V_17 )
incidence_list.append( V_9 )
F_ID = "F_7"
F_7 = onto.function( F_ID )
F_7.is_function_of = incidence_list
V_21.has_function.append( F_7 )
incidence_list = []
incidence_list.append( V_21 )
incidence_list.append( V_3 )
F_ID = "F_27"
F_27 = onto.function( F_ID )
F_27.is_function_of = incidence_list
V_21.has_function.append( F_27 )
#22

V_22.has_function = []
incidence_list = []
incidence_list.append( V_18 )
incidence_list.append( V_9 )
F_ID = "F_8"
F_8 = onto.function( F_ID )
F_8.is_function_of = incidence_list
V_22.has_function.append( F_8 )
incidence_list = []
incidence_list.append( V_22 )
incidence_list.append( V_3 )
F_ID = "F_28"
F_28 = onto.function( F_ID )
F_28.is_function_of = incidence_list
V_22.has_function.append( F_28 )
#23

V_23.has_function = []
incidence_list = []
incidence_list.append( V_19 )
incidence_list.append( V_10 )
F_ID = "F_9"
F_9 = onto.function( F_ID )
F_9.is_function_of = incidence_list
V_23.has_function.append( F_9 )
incidence_list = []
incidence_list.append( V_23 )
incidence_list.append( V_3 )
F_ID = "F_29"
F_29 = onto.function( F_ID )
F_29.is_function_of = incidence_list
V_23.has_function.append( F_29 )
#24

V_24.has_function = []
incidence_list = []
incidence_list.append( V_20 )
incidence_list.append( V_10 )
F_ID = "F_10"
F_10 = onto.function( F_ID )
F_10.is_function_of = incidence_list
V_24.has_function.append( F_10 )
incidence_list = []
incidence_list.append( V_24 )
incidence_list.append( V_3 )
F_ID = "F_30"
F_30 = onto.function( F_ID )
F_30.is_function_of = incidence_list
V_24.has_function.append( F_30 )
#25

V_25.has_function = []
incidence_list = []
incidence_list.append( V_8 )
incidence_list.append( V_80 )
F_ID = "F_11"
F_11 = onto.function( F_ID )
F_11.is_function_of = incidence_list
V_25.has_function.append( F_11 )
#26

V_26.has_function = []
incidence_list = []
incidence_list.append( V_8 )
incidence_list.append( V_81 )
F_ID = "F_12"
F_12 = onto.function( F_ID )
F_12.is_function_of = incidence_list
V_26.has_function.append( F_12 )
#27

V_27.has_function = []
incidence_list = []
incidence_list.append( V_8 )
incidence_list.append( V_82 )
F_ID = "F_14"
F_14 = onto.function( F_ID )
F_14.is_function_of = incidence_list
V_27.has_function.append( F_14 )
#28

V_28.has_function = []
incidence_list = []
incidence_list.append( V_8 )
incidence_list.append( V_83 )
F_ID = "F_15"
F_15 = onto.function( F_ID )
F_15.is_function_of = incidence_list
V_28.has_function.append( F_15 )
#29

V_29.has_function = []
incidence_list = []
incidence_list.append( V_25 )
incidence_list.append( V_26 )
F_ID = "F_16"
F_16 = onto.function( F_ID )
F_16.is_function_of = incidence_list
V_29.has_function.append( F_16 )
incidence_list = []
incidence_list.append( V_29 )
incidence_list.append( V_5 )
F_ID = "F_32"
F_32 = onto.function( F_ID )
F_32.is_function_of = incidence_list
V_29.has_function.append( F_32 )
#30

V_30.has_function = []
incidence_list = []
incidence_list.append( V_27 )
incidence_list.append( V_28 )
F_ID = "F_17"
F_17 = onto.function( F_ID )
F_17.is_function_of = incidence_list
V_30.has_function.append( F_17 )
incidence_list = []
incidence_list.append( V_30 )
incidence_list.append( V_5 )
F_ID = "F_33"
F_33 = onto.function( F_ID )
F_33.is_function_of = incidence_list
V_30.has_function.append( F_33 )
#31

V_31.has_function = []
incidence_list = []
incidence_list.append( V_21 )
incidence_list.append( V_22 )
F_ID = "F_24"
F_24 = onto.function( F_ID )
F_24.is_function_of = incidence_list
V_31.has_function.append( F_24 )
#32

V_32.has_function = []
incidence_list = []
incidence_list.append( V_23 )
incidence_list.append( V_24 )
F_ID = "F_25"
F_25 = onto.function( F_ID )
F_25.is_function_of = incidence_list
V_32.has_function.append( F_25 )
#33

V_33.has_function = []
incidence_list = []
incidence_list.append( V_31 )
incidence_list.append( V_32 )
F_ID = "F_26"
F_26 = onto.function( F_ID )
F_26.is_function_of = incidence_list
V_33.has_function.append( F_26 )
#34

V_34.has_function = []
incidence_list = []
incidence_list.append( V_9 )
incidence_list.append( V_10 )
F_ID = "F_31"
F_31 = onto.function( F_ID )
F_31.is_function_of = incidence_list
V_34.has_function.append( F_31 )
#35

V_35.has_function = []
incidence_list = []
incidence_list.append( V_29 )
incidence_list.append( V_30 )
F_ID = "F_34"
F_34 = onto.function( F_ID )
F_34.is_function_of = incidence_list
V_35.has_function.append( F_34 )
#36

V_36.has_function = []
#50

V_50.has_function = []
#51

V_51.has_function = []
#52

V_52.has_function = []
#53

V_53.has_function = []
#55

V_55.has_function = []
incidence_list = []
incidence_list.append( V_65 )
incidence_list.append( V_64 )
incidence_list.append( V_1 )
incidence_list.append( V_6 )
incidence_list.append( V_7 )
F_ID = "F_48"
F_48 = onto.function( F_ID )
F_48.is_function_of = incidence_list
V_55.has_function.append( F_48 )
#56

V_56.has_function = []
incidence_list = []
incidence_list.append( V_55 )
incidence_list.append( V_3 )
F_ID = "F_44"
F_44 = onto.function( F_ID )
F_44.is_function_of = incidence_list
V_56.has_function.append( F_44 )
#57

V_57.has_function = []
incidence_list = []
incidence_list.append( V_57 )
incidence_list.append( V_3 )
F_ID = "F_51"
F_51 = onto.function( F_ID )
F_51.is_function_of = incidence_list
V_57.has_function.append( F_51 )
#58

V_58.has_function = []
incidence_list = []
incidence_list.append( V_58 )
incidence_list.append( V_3 )
F_ID = "F_52"
F_52 = onto.function( F_ID )
F_52.is_function_of = incidence_list
V_58.has_function.append( F_52 )
#59

V_59.has_function = []
incidence_list = []
incidence_list.append( V_59 )
incidence_list.append( V_3 )
F_ID = "F_53"
F_53 = onto.function( F_ID )
F_53.is_function_of = incidence_list
V_59.has_function.append( F_53 )
#60

V_60.has_function = []
incidence_list = []
incidence_list.append( V_60 )
incidence_list.append( V_3 )
F_ID = "F_54"
F_54 = onto.function( F_ID )
F_54.is_function_of = incidence_list
V_60.has_function.append( F_54 )
#61

V_61.has_function = []
incidence_list = []
incidence_list.append( V_61 )
incidence_list.append( V_3 )
F_ID = "F_61"
F_61 = onto.function( F_ID )
F_61.is_function_of = incidence_list
V_61.has_function.append( F_61 )
incidence_list = []
incidence_list.append( V_75 )
F_ID = "F_62"
F_62 = onto.function( F_ID )
F_62.is_function_of = incidence_list
V_61.has_function.append( F_62 )
#62

V_62.has_function = []
incidence_list = []
incidence_list.append( V_61 )
incidence_list.append( V_3 )
F_ID = "F_45"
F_45 = onto.function( F_ID )
F_45.is_function_of = incidence_list
V_62.has_function.append( F_45 )
#63

V_63.has_function = []
incidence_list = []
incidence_list.append( V_61 )
incidence_list.append( V_62 )
F_ID = "F_46"
F_46 = onto.function( F_ID )
F_46.is_function_of = incidence_list
V_63.has_function.append( F_46 )
#64

V_64.has_function = []
incidence_list = []
incidence_list.append( V_50 )
incidence_list.append( V_55 )
incidence_list.append( V_51 )
incidence_list.append( V_63 )
F_ID = "F_47"
F_47 = onto.function( F_ID )
F_47.is_function_of = incidence_list
V_64.has_function.append( F_47 )
#65

V_65.has_function = []
#66

V_66.has_function = []
#67

V_67.has_function = []
incidence_list = []
incidence_list.append( V_52 )
incidence_list.append( V_55 )
incidence_list.append( V_66 )
incidence_list.append( V_65 )
incidence_list.append( V_53 )
incidence_list.append( V_63 )
F_ID = "F_49"
F_49 = onto.function( F_ID )
F_49.is_function_of = incidence_list
V_67.has_function.append( F_49 )
incidence_list = []
incidence_list.append( V_52 )
incidence_list.append( V_55 )
incidence_list.append( V_68 )
incidence_list.append( V_63 )
F_ID = "F_50"
F_50 = onto.function( F_ID )
F_50.is_function_of = incidence_list
V_67.has_function.append( F_50 )
#68

V_68.has_function = []
#69

V_69.has_function = []
incidence_list = []
incidence_list.append( V_57 )
incidence_list.append( V_58 )
F_ID = "F_55"
F_55 = onto.function( F_ID )
F_55.is_function_of = incidence_list
V_69.has_function.append( F_55 )
#70

V_70.has_function = []
incidence_list = []
incidence_list.append( V_59 )
incidence_list.append( V_60 )
F_ID = "F_56"
F_56 = onto.function( F_ID )
F_56.is_function_of = incidence_list
V_70.has_function.append( F_56 )
#71

V_71.has_function = []
incidence_list = []
incidence_list.append( V_69 )
incidence_list.append( V_70 )
F_ID = "F_57"
F_57 = onto.function( F_ID )
F_57.is_function_of = incidence_list
V_71.has_function.append( F_57 )
#72

V_72.has_function = []
incidence_list = []
incidence_list.append( V_21 )
incidence_list.append( V_3 )
F_ID = "F_58"
F_58 = onto.function( F_ID )
F_58.is_function_of = incidence_list
V_72.has_function.append( F_58 )
#73

V_73.has_function = []
#74

V_74.has_function = []
incidence_list = []
incidence_list.append( V_72 )
incidence_list.append( V_21 )
F_ID = "F_59"
F_59 = onto.function( F_ID )
F_59.is_function_of = incidence_list
V_74.has_function.append( F_59 )
#75

V_75.has_function = []
incidence_list = []
incidence_list.append( V_73 )
incidence_list.append( V_74 )
F_ID = "F_60"
F_60 = onto.function( F_ID )
F_60.is_function_of = incidence_list
V_75.has_function.append( F_60 )
#76

V_76.has_function = []
incidence_list = []
incidence_list.append( V_76 )
incidence_list.append( V_3 )
F_ID = "F_63"
F_63 = onto.function( F_ID )
F_63.is_function_of = incidence_list
V_76.has_function.append( F_63 )
incidence_list = []
incidence_list.append( V_67 )
F_ID = "F_70"
F_70 = onto.function( F_ID )
F_70.is_function_of = incidence_list
V_76.has_function.append( F_70 )
#77

V_77.has_function = []
incidence_list = []
incidence_list.append( V_17 )
incidence_list.append( V_18 )
F_ID = "F_64"
F_64 = onto.function( F_ID )
F_64.is_function_of = incidence_list
V_77.has_function.append( F_64 )
incidence_list = []
incidence_list.append( V_69 )
F_ID = "F_67"
F_67 = onto.function( F_ID )
F_67.is_function_of = incidence_list
V_77.has_function.append( F_67 )
#78

V_78.has_function = []
incidence_list = []
incidence_list.append( V_19 )
incidence_list.append( V_20 )
F_ID = "F_65"
F_65 = onto.function( F_ID )
F_65.is_function_of = incidence_list
V_78.has_function.append( F_65 )
incidence_list = []
incidence_list.append( V_70 )
F_ID = "F_68"
F_68 = onto.function( F_ID )
F_68.is_function_of = incidence_list
V_78.has_function.append( F_68 )
#79

V_79.has_function = []
incidence_list = []
incidence_list.append( V_77 )
incidence_list.append( V_78 )
F_ID = "F_66"
F_66 = onto.function( F_ID )
F_66.is_function_of = incidence_list
V_79.has_function.append( F_66 )
incidence_list = []
incidence_list.append( V_71 )
F_ID = "F_69"
F_69 = onto.function( F_ID )
F_69.is_function_of = incidence_list
V_79.has_function.append( F_69 )
#80

V_80.has_function = []
incidence_list = []
incidence_list.append( V_76 )
incidence_list.append( V_13 )
incidence_list.append( V_36 )
incidence_list.append( V_21 )
F_ID = "F_75"
F_75 = onto.function( F_ID )
F_75.is_function_of = incidence_list
V_80.has_function.append( F_75 )
incidence_list = []
incidence_list.append( V_80 )
incidence_list.append( V_3 )
F_ID = "F_79"
F_79 = onto.function( F_ID )
F_79.is_function_of = incidence_list
V_80.has_function.append( F_79 )
#81

V_81.has_function = []
incidence_list = []
incidence_list.append( V_14 )
incidence_list.append( V_36 )
incidence_list.append( V_22 )
F_ID = "F_76"
F_76 = onto.function( F_ID )
F_76.is_function_of = incidence_list
V_81.has_function.append( F_76 )
incidence_list = []
incidence_list.append( V_81 )
incidence_list.append( V_3 )
F_ID = "F_80"
F_80 = onto.function( F_ID )
F_80.is_function_of = incidence_list
V_81.has_function.append( F_80 )
#82

V_82.has_function = []
incidence_list = []
incidence_list.append( V_15 )
incidence_list.append( V_36 )
incidence_list.append( V_23 )
F_ID = "F_77"
F_77 = onto.function( F_ID )
F_77.is_function_of = incidence_list
V_82.has_function.append( F_77 )
incidence_list = []
incidence_list.append( V_82 )
F_ID = "F_81"
F_81 = onto.function( F_ID )
F_81.is_function_of = incidence_list
V_82.has_function.append( F_81 )
#83

V_83.has_function = []
incidence_list = []
incidence_list.append( V_16 )
incidence_list.append( V_36 )
incidence_list.append( V_24 )
F_ID = "F_78"
F_78 = onto.function( F_ID )
F_78.is_function_of = incidence_list
V_83.has_function.append( F_78 )
incidence_list = []
incidence_list.append( V_83 )
incidence_list.append( V_3 )
F_ID = "F_82"
F_82 = onto.function( F_ID )
F_82.is_function_of = incidence_list
V_83.has_function.append( F_82 )

onto.save("variables.owl")
