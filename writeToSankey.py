# row format: source, target, volume

def writeToSankey(row):
    # skmt is a sankeymatic file (not officially)
    with open("out/sankey.skmt", "a") as file:
        file.write("{} [{}] {}\n".format(row["Source"], row["Volume"], row["Target"]))
    return