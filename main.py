BOY = ";"
class TIMESTAMP:
    weekday = ""
    hour = ""
    consumption = 0.0
    price = 0.0
def readTimestamps(filename, timestamps):
    print('Reading file "' + filename + '".')
    timestamps.clear()
    filehandle = open(filename, "r", encoding="utf-8")
    Skipper2 = filehandle.readline()
    while True:
        line = filehandle.readline()
        if len(line) == 0:
            break
        clean_line = line.strip()
        if len(clean_line) > 0:
            cols = clean_line.split(BOY)
            stamp = TIMESTAMP()
            stamp.weekday = cols[0]
            stamp.hour = cols[1]
            stamp.consumption = float(cols[2])
            stamp.price = float(cols[3])
            timestamps.append(stamp)
            cols.clear()
    filehandle.close()
    return None
def displayTimestamps(timestamps):
    print("Electricity usage:")
    for i in range(len(timestamps)):
        stamp = timestamps[i]
        total = stamp.consumption * stamp.price
        price_str = "{0:.2f}".format(stamp.price)
        cons_str = "{0:.2f}".format(stamp.consumption)
        total_str = "{0:.2f}".format(total)
        print(" - " + stamp.weekday + " " + stamp.hour + ":00, price " + price_str + ", consumption " + cons_str + " kwh, total " + total_str + " €")
    return None
def main():
    print("Program starting.")
    timestamps = []
    filename = input("Insert filename: ")
    readTimestamps(filename, timestamps)
    displayTimestamps(timestamps)
    timestamps.clear()
    print("Program ending.")
    return None
main()