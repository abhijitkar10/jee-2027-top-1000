# Build progress (working notes)

Pipeline: MathonGo PDF of NTA paper (via Firecrawl, `parsers:["pdf"]`) -> rebuild question text from
extracted text + formula fragments -> independently re-solve -> keep only if it matches the key on the
last page of the PDF -> `scripts/ingest.py` -> `scripts/build.py --write` (renumber + validate).

Skip: questions that depend on a figure/structure image, or where the text cannot be rebuilt confidently.

## Papers done
- JEE Main 2024 · 27 Jan S1 (Qe0X), 27 Jan S2 (2rtB), 29 Jan S1 (Oe6L)

## MathonGo short links (order on index page; label from the PDF header)
2024 Jan: Qe0X 2rtB Oe6L Be5F ZrrZ urqP 0rqQ YreE JeHi EeXb
2024 Apr: 1eFi ke3T Qe4c ve7K be1q We8M Te2Q UeMQ QeNi Ee9x
2023 Jan: FeSn 0eGa reDl ueKo 9eZR NeJV WeCF 7eLF teB4 teVX Wecg qevi
2023 Apr: CemG VeIY AePp ueOJ peTO 8eYy heA9 peEc jeUu 8eR2 7eQ6 veWO
2022 Jun: 6ews FeeC cw64 UerM 7eaY Oep9 hege zefX sen0 sexw gebc zezZ
2022 Jul: keij Rw5W Heu7 kedY wese qejq Geoa AehM Eels QekQ
(JEE Advanced: https://jeeadv.ac.in/past_qps/<year>_<paper>_English.pdf)
