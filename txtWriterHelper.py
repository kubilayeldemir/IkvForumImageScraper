def write_to_later_list(logfileName, logText):
    f = open(logfileName, "a")
    f.write(str(logText))
    f.write("\n")
    f.close()
