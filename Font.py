# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import tkinter as tk
from tkinter import *

def Font_size(Name,Text):

	x_val = Text

	def _8():
		return x_val.config(font=("segoe ui",8))

	def _9():
		return x_val.config(font=("segoe ui",9))

	def _10():
		return x_val.config(font=("segoe ui",10))

	def _11():
		return x_val.config(font=("segoe ui",11))

	def _12():
		return x_val.config(font=("segoe ui",12))

	def _14():
		return x_val.config(font=("segoe ui",14))

	def _16():
		return x_val.config(font=("segoe ui",16))

	def _18():
		return x_val.config(font=("segoe ui",18))

	def _20():
		return x_val.config(font=("segoe ui",20))

	def _22():
		return x_val.config(font=("segoe ui",22))

	def _24():
		return x_val.config(font=("segoe ui",24))

	def _26():
		return x_val.config(font=("segoe ui",26))

	def _28():
		return x_val.config(font=("segoe ui",28))

	def _36():
		return x_val.config(font=("segoe ui",36))

	def _48():
		return x_val.config(font=("segoe ui",48))

	def _72():
		return x_val.config(font=("segoe ui",72))

	Font_size = Menu(Name, tearoff=0)
	Font_size.add_command(label="8", command=_8)
	Font_size.add_separator()
	Font_size.add_command(label="9", command=_9)
	Font_size.add_separator()
	Font_size.add_command(label="10", command=_10)
	Font_size.add_separator()
	Font_size.add_command(label="11", command=_11)
	Font_size.add_separator()
	Font_size.add_command(label="12", command=_12)
	Font_size.add_separator()
	Font_size.add_command(label="14", command=_14)
	Font_size.add_separator()
	Font_size.add_command(label="16", command=_16)
	Font_size.add_separator()
	Font_size.add_command(label="18", command=_18)
	Font_size.add_separator()
	Font_size.add_command(label="20", command=_20)
	Font_size.add_separator()
	Font_size.add_command(label="22", command=_22)
	Font_size.add_separator()
	Font_size.add_command(label="24", command=_24)
	Font_size.add_separator()
	Font_size.add_command(label="26", command=_26)
	Font_size.add_separator()
	Font_size.add_command(label="28", command=_28)
	Font_size.add_separator()
	Font_size.add_command(label="36", command=_36)
	Font_size.add_separator()
	Font_size.add_command(label="48", command=_48)
	Font_size.add_separator()
	Font_size.add_command(label="72", command=_72)

	return Font_size