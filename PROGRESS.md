# Build progress (working notes)

Pipeline: MathonGo PDF of NTA paper (via Firecrawl, `parsers:["pdf"]`) -> rebuild question text from
extracted text + formula fragments -> independently re-solve -> keep only if it matches the key on the
last page of the PDF -> `scripts/ingest.py` -> `scripts/build.py --write` (renumber + validate).

Skip: questions that depend on a figure/structure image, or where the text cannot be rebuilt confidently.

## Papers done
- JEE Main 2024 · 27 Jan S1 (Qe0X), 27 Jan S2 (2rtB), 29 Jan S1 (Oe6L), 29 Jan S2 (Be5F), 30 Jan S1 (ZrrZ; physics done, chem+maths pending)

## MathonGo short links (order on index page; label from the PDF header)
2024 Jan: Qe0X 2rtB Oe6L Be5F ZrrZ urqP 0rqQ YreE JeHi EeXb
2024 Apr: 1eFi ke3T Qe4c ve7K be1q We8M Te2Q UeMQ QeNi Ee9x
2023 Jan: FeSn 0eGa reDl ueKo 9eZR NeJV WeCF 7eLF teB4 teVX Wecg qevi
2023 Apr: CemG VeIY AePp ueOJ peTO 8eYy heA9 peEc jeUu 8eR2 7eQ6 veWO
2022 Jun: 6ews FeeC cw64 UerM 7eaY Oep9 hege zefX sen0 sexw gebc zezZ
2022 Jul: keij Rw5W Heu7 kedY wese qejq Geoa AehM Eels QekQ
(JEE Advanced: https://jeeadv.ac.in/past_qps/<year>_<paper>_English.pdf)

## Fetch trick (much cleaner extraction than the Drive viewer)
1. `firecrawl_scrape` a links.mathongo.com short link with `formats:["links"], onlyMainContent:true` -> metadata.url has the Drive file id.
2. `firecrawl_scrape https://drive.google.com/uc?export=download&id=<ID>` with `parsers:["pdf"]`, `pdfOptions.maxPages:20`.
Drive ids resolved so far: 30Jan S1 1GUD1oORrilgLN6wtNt8CzWVRlZecIUOC, 30Jan S2 1ma1FxjJa3ZYwGlmcOi3zweRgtYjV7gxO,
31Jan S1 1dprC6kH74hITrqAxEg8QvSktsB0A_HjO, 31Jan S2 1zFWJi00C3Fweusixago3A-1yl1LsqFPr,
1Feb S1 11TKs1Sf7flPoF2i8KElBsRGjm_Lk3Jm8, 1Feb S2 1a-M47RCdSI6JYikiWmqG5Lnt0C8sLi_r,
4Apr S1 1C3eYdfTXtkUyxjQSIdiW89U5-KIFrEOF, 4Apr S2 1szZ2LieKVHhLVyksv3p5ldN_XB0Fo98s, 5Apr S1 1EE_vPu11xciFvd1zMgkYYmSg0uJr5Hbe
