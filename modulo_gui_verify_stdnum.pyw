#!/usr/bin/env python3
# -*- coding: cp1252 -*-
# https://arthurdejong.org/python-stdnum/
# https://pypi.org/project/python-stdnum/

"""
****************************************************************************
 This Program provides a GUI for the ISO 7064 Modulo 11/10 Checksum Algorithm.
 Copyright (C) 2021, Fabian D. Tröster
 This is free software; you can redistribute it and/or modify it under the
 terms of the GNU General Public License, either Version 2 or any later
 version.  This program is distributed in the hope that it will be useful,
 but WITTHOUT ANY WARRANTY.
*****************************************************************************
"""

import tkinter as tk
import tkinter.messagebox as mb
import stdnum.iso7064.mod_11_10 as md

top = tk.Tk()
vl = tk.StringVar(top)
cs = tk.StringVar(top)
rs = tk.StringVar(top)
vll = tk.StringVar(top)
rel = tk.StringVar(top)


def modulo_gui():
    l1 = tk.Label(top, text="Input")
    l2 = tk.Label(top, text="Output")

    value = tk.Entry(top, width=20, textvariable=vl)
    check_sum = tk.Entry(top, width=2, textvariable=cs)
    len_val = tk.Entry(top, width=2, state=tk.DISABLED, textvariable=vll)
    result = tk.Entry(top, width=23, state=tk.DISABLED, textvariable=rs)
    len_res = tk.Entry(top, width=2, state=tk.DISABLED, textvariable=rel)

    start_calc = tk.Button(top, text="Calculate Checkdigit", command=start_calculation)
    verify = tk.Button(top, text="Verify Checkdigit (F2)", command=verify_digit)
    csclip = tk.Button(top, text="Copy Checkdigit", command=copy_cs_to_clipboard)
    rsclip = tk.Button(top, text="Copy Result", command=copy_rs_to_clipboard)
    clear = tk.Button(top, text="Clear Entries (F3)", command=clear_entry)
    cl_cd = tk.Button(top, text="Clear Checkdigit (F4)", command=clear_digit)
    cnt_len = tk.Button(top, text="Length", command=count_length)
    
    about = tk.Button(top, text="About...", command=call_about_dlg)


    top.title("Modulo 11-10 (ISO 7064) with Verify")

    top.bind("<Return>", start_calc)
    top.bind("<F2>", verify_dig)
    top.bind("<F3>", clr_entry)
    top.bind("<F4>", clr_digit)

    l1.grid(row=0, column=0, sticky=tk.W)
    l2.grid(row=1, column=0, sticky=tk.W)

    value.grid(row=0, column=1)
    check_sum.grid(row=0, column=2)
    len_val.grid(row=0, column=3)
    
    result.grid(row=1, column=1, columnspan=2)
    len_res.grid(row=1, column=3)

    value.focus()

    start_calc.grid(row=0, column=4)
    verify.grid(row=1, column=4)
    csclip.grid(row=0, column=5)
    rsclip.grid(row=1, column=5)
    clear.grid(row=0, column=6)
    cl_cd.grid(row=1, column=6)
    cnt_len.grid(row=0, column=7)

    about.grid(row=1, column=7)

    top.mainloop()


def start_calc(event):
    start_calculation()


def verify_dig(event):
    verify_digit()


def clr_entry(event):
    clear_entry()


def clr_digit(event):
    clear_digit()


def start_calculation():
    if vl.get() != "":
        cs.set(md.calc_check_digit(vl.get()))
        rs.set(vl.get() + cs.get())
        vll.set(len(vl.get()))
        rel.set(len(rs.get()))
    pass


def clear_entry():
    vl.set("")
    cs.set("")
    rs.set("")
    vll.set("")
    rel.set("")


def copy_cs_to_clipboard():
    start_calculation
    top.clipboard_clear()
    top.clipboard_append(cs.get())


def copy_rs_to_clipboard():
    start_calculation()
    top.clipboard_clear()
    top.clipboard_append(rs.get())


def verify_digit():
    vll.set("")
    rel.set("")
    if vl.get() != "" and cs.get() != "":
        if (md.is_valid(vl.get() + cs.get())):
            rs.set("Correct Checkdigit")
        else:
            rs.set("Incorrect Checkdigit")
    else:
        rs.set("Fill both Inputs")


def clear_digit():
    cs.set("")
    rs.set("")
    vll.set("")
    rel.set("")


def call_about_dlg():
    mb.showinfo("About", "2015 - 2021\nFabian D. Tröster")


def count_length():
    if vl.get() != "":
        vll.set(len(vl.get()))
    pass


if __name__ == "__main__":
    modulo_gui()
