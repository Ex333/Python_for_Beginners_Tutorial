# You have been hired to create onboard software for a modern car.
# Your current task is to program the controller responsible for automatically
# switching on the low-beam headlights.

# We will work with the following variables:

# isAutomaticMode - Boolean variable.
# True means that the driver has set the light control knob to automatic mode.
# The controller should make a decision about turning the lights on only
# when this variable is True.

# is80PercentLight - Boolean variable.
# True means that there is probably daylight because there is enough light outside.
# The car lights should remain off unless there are other conditions
# that require them to be turned on.
# False means that it is dark enough and the lights should be turned on,
# provided that automatic mode is enabled.

# isDirectLight - Boolean variable.
# True means that the low-positioned sun is shining directly into the driver's eyes.
# Although it is not dark, the lights should be turned on in these conditions,
# provided that automatic mode is enabled.

# isRainy - Boolean variable.
# True means that it is raining, foggy, or there are other unfavorable weather conditions.
# If automatic mode is enabled, the lights should be turned on.

# Store the result of the expression in the turnLightsOn variable.
# The expression should determine whether the lights should be turned on
# based on the variables described above.

# Then display the results using the following instructions:

# print("Automatic mode:   ", isAutomaticMode)
# print("Is the light good:", is80PercentLight)
# print("Is sun low:       ", isDirectLight)
# print("Is it rainy:      ", isRainy)
# print("TURN LIGHTS ON:   ", turnLightsOn)


# Test the expression by changing the initial values of the input variables.

# Test 1:
# Automatic mode is enabled.
# There is more than 80% daylight.
# The sun is not shining directly into the driver's face.
# It is not rainy or foggy.
# Expected result: the lights should NOT be turned on.

isAutomaticMode = True
is80PercentLight = True
isDirectLight = False
isRainy = False
turnLightsOn = isAutomaticMode and not is80PercentLight or isDirectLight or isRainy

print("Automatic mode:   ", isAutomaticMode)
print("Is the light good:", is80PercentLight)
print("Is sun low:       ", isDirectLight)
print("Is it rainy:      ", isRainy)
print("TURN LIGHTS ON:   ", turnLightsOn)

# Expected: turnLightsOn = False


# Test 2:
# Automatic mode is enabled.
# There is not enough daylight.
# The sun is not shining directly into the driver's face.
# It is not rainy or foggy.
# Expected result: the lights should be turned on.

isAutomaticMode = True
is80PercentLight = False
isDirectLight = False
isRainy = False

turnLightsOn = isAutomaticMode and not is80PercentLight or isDirectLight or isRainy

print("Automatic mode:   ", isAutomaticMode)
print("Is the light good:", is80PercentLight)
print("Is sun low:       ", isDirectLight)
print("Is it rainy:      ", isRainy)
print("TURN LIGHTS ON:   ", turnLightsOn)

# Expected: turnLightsOn = True


# Test 3:
# Automatic mode is enabled.
# There is enough daylight.
# The sun is not shining directly into the driver's face.
# It is rainy or foggy.
# Expected result: the lights should be turned on.

isAutomaticMode = True
is80PercentLight = True
isDirectLight = False
isRainy = True

turnLightsOn = isAutomaticMode and not is80PercentLight or isDirectLight or isRainy

print("Automatic mode:   ", isAutomaticMode)
print("Is the light good:", is80PercentLight)
print("Is sun low:       ", isDirectLight)
print("Is it rainy:      ", isRainy)
print("TURN LIGHTS ON:   ", turnLightsOn)

# Expected: turnLightsOn = True


# Test 4:
# Automatic mode is enabled.
# There is enough daylight.
# The sun is shining directly into the driver's face.
# It is not rainy or foggy.
# Expected result: the lights should be turned on.

isAutomaticMode = True
is80PercentLight = True
isDirectLight = True
isRainy = False

turnLightsOn = isAutomaticMode and not is80PercentLight or isDirectLight or isRainy

print("Automatic mode:   ", isAutomaticMode)
print("Is the light good:", is80PercentLight)
print("Is sun low:       ", isDirectLight)
print("Is it rainy:      ", isRainy)
print("TURN LIGHTS ON:   ", turnLightsOn)

# Expected: turnLightsOn = True


# Test 5:
# Automatic mode is enabled.
# There is not enough daylight.
# The sun is not shining directly into the driver's face.
# It is rainy or foggy.
# Expected result: the lights should be turned on.

isAutomaticMode = True
is80PercentLight = False
isDirectLight = False
isRainy = True

turnLightsOn = isAutomaticMode and not is80PercentLight or isDirectLight or isRainy

print("Automatic mode:   ", isAutomaticMode)
print("Is the light good:", is80PercentLight)
print("Is sun low:       ", isDirectLight)
print("Is it rainy:      ", isRainy)
print("TURN LIGHTS ON:   ", turnLightsOn)

# Expected: turnLightsOn = True


# Test 6:
# Automatic mode is disabled.
# There is enough daylight.
# The sun is not shining directly into the driver's face.
# It is rainy or foggy.
# Expected result: the lights should NOT be turned on,
# because automatic mode is disabled.

isAutomaticMode = False
is80PercentLight = True
isDirectLight = False
isRainy = True

turnLightsOn = isAutomaticMode and (
    not is80PercentLight or isDirectLight or isRainy
)

print("Automatic mode:   ", isAutomaticMode)
print("Is the light good:", is80PercentLight)
print("Is sun low:       ", isDirectLight)
print("Is it rainy:      ", isRainy)
print("TURN LIGHTS ON:   ", turnLightsOn)

# Expected: turnLightsOn = False