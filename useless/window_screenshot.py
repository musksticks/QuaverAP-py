import mss

with mss.mss() as sct:  # Create a new mss.mss instance
    monitor = {"top": 500, "left": 680, "width": 560, "height": 485}
    output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

    sct_img = sct.grab(monitor)

    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)