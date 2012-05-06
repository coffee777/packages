#!/bin/awk -f

# This script executes .gschema.override files directly with the gsettings
# command line utility, instead of installing and recompiling the schemas.


# Initialise counters
BEGIN {
    keycount = 0
    schemacount = 0
}

# Keep track of schema headings
/^\[(.*)\]$/ {
    schema = substr($0, 2, length($0)-2)
    schemacount += 1
    next
}

# Double quote arrays of single quoted strings
/^[a-z-]*=\['/ {
    sub(/\[/, "\"[")
    sub(/\]/, "]\"")
}

# Single quote arrays of double quoted strings
/^[a-z-]*=\["/ {
    sub(/\[/, "'[")
    sub(/\]/, "]'")
}

# Replace first equals with a space and send command to shell
/^[a-z-]*=/ {
    if (schema == "") {
        print "ERROR: key without section on line " NR
        exit 1
    }
    sub(/=/, " ")
    system("gsettings set " schema " " $0)
    keycount += 1
    next
}

# If anything except blank lines get this far we've got an error
/.+/ {
    print "ERROR on line " NR ":\n>  " $0
    exit 1
}

# Print summary
END {
    print "set " keycount " keys in " schemacount " schemas"
}
