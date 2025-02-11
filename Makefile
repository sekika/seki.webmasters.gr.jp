all: up

up:
	rsync -av --exclude .git ./ swatch:public_html/

