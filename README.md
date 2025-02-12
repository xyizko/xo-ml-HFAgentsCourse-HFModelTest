
<p align="center"><a href="https://x.com/xyizko" target="_blank" rel="noopener noreferrer"><img src="https://raw.githubusercontent.com/xyizko/xo-tagz/refs/heads/main/gfx/a.png"></a></p>

<p align="center">
<a href="https://twitter.com/xyizko" target="_blank">
<img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fxyizko%2Fxo-ml-HFAgentsCourse-HFModelTest&count_bg=%23E6008B&title_bg=%23000000&icon=teamspeak.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false"/>
</a>
</p>


<h1 align="center"><code> xo-ml-HFAgentsCourse-HFModelTest </code></h1>
<h2 align="center"><i> Simple Python APP made for testing HuggingFace Models access via API </i></h2>

1. [Demo](#demo)
2. [What ?](#what-)
3. [How](#how)
4. [Warning](#warning)

# Demo

![](./gfx/demo.gif)


# What ? 

> Simple python app for testing the various models in HuggingFace via the API 

# How 

> Note this repo uses [`uv`](https://docs.astral.sh/uv/). Install this first.

1. Clone Repo 
2. Inside `src/` make a file `.env` and add your _HugginFace Api_ 
3. execute `uv run xo.py`
4. Results will be displayed in the console as well as written to a directory called `rez/` with a markdown file which has the current date and time appended to it. 
5. The testing was done on 2 free models. But you can use any model which is being hosted on the Inference API. 
6. The results displayed in the console has debugging statements to examine the connection to the API

# Warning

> This repo is an experiment

![](./gfx/e.webp)
