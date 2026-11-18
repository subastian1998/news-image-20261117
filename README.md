# news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/subastian1998/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/subastian1998/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

A make.fun bounty entry for
[Sum up 17 November's world news in one image](https://make.fun/bounty/news-image-20261117):
one 1024×1024 PNG front page that sums up the day's world news.

## How the program works

`main.py` (Python 3.13, standard library only) copies the `entry.png`
beside it to `/output/entry.png` — no network, no timestamps, no
randomness, so the two grader runs write byte-identical output.
Outside the grader, `MAKEFUN_OUTPUT_DIR` stands in for `/output`:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Stories covered

- **Lead — War in the Gulf escalates:** a fourth tanker is hit by a mine
  in the Strait of Hormuz in 24 hours; Iran's navy seizes a US drone;
  a third US carrier, USS Theodore Roosevelt, reaches the Middle East.
- **Ukraine strikes Kerch Bridge:** the Crimean Bridge is severely damaged
  and traffic suspended; Russia hits bridges in Kyiv; a strike on
  Zaporizhzhia kills 40.
- **Xi, Trump & Putin to meet:** a first-ever three-way summit is set for
  Thursday in Shenzhen, on the APEC sidelines.
- **Gaza — West urges open crossings:** Britain, Australia, Canada and
  Italy call on Israel to let aid in fast; an Israeli strike on Gaza tents
  kills three.
- **COP31 draft deal:** Antalya talks call for a faster fossil-fuel
  phase-out and $120bn a year in climate finance by 2035.
- **Japan scrambles jets:** after suspected Russian aircraft violate its
  airspace.
- **In brief:** Bitcoin stalls below $65,000; the US loses measles
  elimination status; a JPMorgan banking outage blamed on a software bug;
  India beat Pakistan in the U19 Asia Cup final.

## The image

`entry.png` — 1024×1024 PNG, drawn with PIL (DejaVu fonts): a
newspaper front page with a masthead dated **Tuesday 17 November 2026**,
a lead panel with a labelled tanker / mine / drone / carrier diagram,
four story panels with small drawn icons, and an "In brief" footer strip.
The image was drawn once, by hand, with a local PIL script; the program
itself only copies the finished file, so what the judge sees is exactly
the bytes in this repository.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=7gw1p7j6&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
