#!/bin/sh
# Make the card images from the ungraded originals in sources/cards/: one consistent cinematic grade
# (deeper contrast, slightly lower saturation, cool shadows, warm highlights, a soft vignette, light grain),
# written as assets/home/work/<name>@2x.jpg (up to 2048 px) and <name>.jpg (1024 px). Needs ffmpeg.
# Run from the repo root:  sh scripts/grade_cards.sh
set -e
GRADE="eq=contrast=1.14:saturation=0.86:brightness=-0.025:gamma=0.97,colorbalance=rs=-0.05:gs=-0.01:bs=0.06:rm=0.01:bm=-0.01:rh=0.06:gh=0.025:bh=-0.05,vignette=angle=PI/4.6,noise=alls=5:allf=u"
for src in sources/cards/*.jpg; do
  name=$(basename "$src" .jpg)
  ffmpeg -loglevel error -y -i "$src" -vf "scale='min(2048,iw)':-2,$GRADE" -q:v 3 "assets/home/work/$name@2x.jpg"
  ffmpeg -loglevel error -y -i "assets/home/work/$name@2x.jpg" -vf "scale=1024:-2" -q:v 3 "assets/home/work/$name.jpg"
  echo "graded $name"
done
