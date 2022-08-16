```
+------------------------------------------------------------------------------+
|                                                                              |
|                          Snooping as usual,  I see?                          |
|                              ¯¯¯¯¯¯¯                                         |
|           ""|""""".     .-"""-.    ""|""""".    """|"""   .-"""-.TM          |
|             |      \   /       \     |      \      |     /       V           |
|             |      /  |         |    |      /      |     \                   |
|             |_____/   |         |    |_____/       |      ""---__            |
|             |     \   |         |    |'.           |             \           |
|             |      \  |         |    |  '.         |             |           |
|             |      /   \       /     |    '.       |     N       /           |
|           __|____.'     '-___-'    __|__  __\_  ___|___  |'-___-'            |
|                                                                              |
|                   The New Textmode Editor  for the New Era                   |
|                  written in Python 3.10 | by Katsumi Kougen                  |
|                                                                              |
|         |  | /""\ |""" |""\    |\ /|    ^    |\  | |  |    ^    |            |
|         |  | '-_  |__  |__/    | V |   / \   | \ | |  |   / \   |            |
|         |  |    | |    |'.     |   |  /---\  |  \| |  |  /---\  |            |
|         \__/ \__/ |___ |  \    |   | /     \ |   | \__/ /     \ |___         |
|                                                                              |
+------------------------------------------------------------------------------+
```

# Introduction

Oh, hello there!

Welcome to ***Boris*' User Manual**. The purpose of this manual is to show you how to use the text mode editor *Boris* as well as the concept of text mode art (or ASCII art or whatever sh\*t you wanna call).

So, without further ado, let's get started!

```
            .-------.
           (""""-----)                 |"""""""""""""|
            \_/\__/\/                  |  Squadala!  |
           < (|)(|)  >                 |  We're off! |
           <__ VV __>       ______----""__-----------'
    .__     -_\';|__       __"""""""""""
     '-==\""" \\:// """"/=-'
        | |    \|/    ||
        "-"""|  V  |"""
             / /   |
   .-""""""";------(""".-'
.-'        (___/___).-'
""""""""""""""""""""
```

# Getting Started

## Before running *Boris*...

*Boris* is written in Python 3.10, and therefore takes advantage of Python 3.10's features. If you want to run the program, you need to have Python 3.10 installed on your computer.

If you already have Python 3.10 installed, you're good to go. If not, go install it [here](https://python.org). As a reminder to Windows users, Python 3.10 won't run on Windows 7 or earlier. If your PC runs Windows 7 or earlier, tough sh\*t.

*Boris* uses these following libraries: *tkinter*, *clipboard*, and *Pillow*. The former is bundled with Python 3, but the latter two have to be installed manually.

## Introduction to text mode art/ASCII art

### [What the f\*ck is a "textmode"?](https://www.youtube.com/watch?v=ZB0fDrpmKTg)

Text mode art is a broad term for art made with a monospaced font on a uniform grid. The term arose from a need to categorise art that didn't use a specific specification.

In the same way that "tile art" encapsulates pixelart, mosaic, sprite art, "text mode art" covers a great many different subcategories. Textmode encapsulates art like ASCII (not [AZKi](https://www.youtube.com/channel/UC0TXe_LYZ4scaW2XMyi5_kw)), ANSI, PETSCII and many others which have their own specific restrictions.

Old computers used to have various modes for displaying graphics — with high resolution modes for displaying pixel art with varying degrees of colour, and often a text mode for displaying uniform tiles of text characters in units of one character, one foreground colour and one background colour. This was beneficial because it required less RAM to display large, colourful graphics.<sup>`[1]`</sup>

Let me show you how text mode actually works, in case you still don't understand. We'll start with the text mode on the CGA:

> To show graphics on the screen, your graphics card needs to have memory. Otherwise it would forget instantly what it should be drawing. 
It has to remember every detail that is on the screen.
>
> Modern graphics cards have thousands of millions of bytes of memory on them, but things were very different with early graphics cards.
>
> The CGA, which came with the original IBM PC, only had sixteen kilobytes of memory. That's literally hundreds of thousands times less than a typical graphics card on the market today.
>
> The text mode display on the CGA is made of 80 character cells side by side, on 25 distinct rows. Each of these cells is eight pixels wide, and eight pixels tall. If we do some quick mathematics, that's 128000 pixels. Furthermore, each of these characters can have 16 distinct colours for both the foreground and the background. If this data was indeed represented as pixels, this would mean four bits per pixel, and the total would therefore be 512000 bits, or 64000 bytes. The poor CGA definitely did not have that much memory. 😵‍💫️ It only had 16000 bytes, enough for only monochrome graphics at this resolution.
>
> To get around this problem, they stored the text mode data differently. Instead of storing each individual pixel in the memory, they would only store character cells. Each of these 80×25 cells can only have one of 256 possible character symbols. Additionally there is an attribute for each cell; the attribute can specify one of 16 distinct different foreground colours and 8 distinct background colours, either blinking or not blinking. If we do some quick mathematics, that's 80 ⋅ 25 ⋅ (1 + 1) = 4000 bytes = 4 kilobytes, which is adequate enough for the CGA. Yes, 1000 bytes is one kilobyte. *(You wanna start a debate? Read [this](https://en.wikipedia.org/wiki/Kilobyte#Definitions_and_usage) first.)*
>
> Unfortunately, this means that you cannot show arbitrary graphics in this mode. That's what the "*only*" in "*text-**only** mode*" refers to. These 256 characters are what you have, that's all. Of course some of these symbols are not so much text, and clever souls were able to utilize it for cool graphics.<sup>`[2]`</sup>

In a nutshell, text mode art is a general term for tile art which is:

* Created from a fixed two colour tileset (usually a 1-bit font)
* On a uniform grid
* With at most a single foreground and background colour per character<sup>`[1]`</sup>

> **References:**
>
> * `[1]` ["*What is textmode?*" — Polyducks](http://polyducks.co.uk/what-is-textmode/)
> * `[2]` ["How I got Mario in That Editor — And how Norton got 🐁" — ](https://www.youtube.com/watch?v=7nlNQcKsj74)[Joel "Bisqwit" Yliluoma](https://bisqwit.iki.fi)
