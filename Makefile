.PHONY: check search
check:
	python3 scripts/direction_filter.py --gene BUB1B
search:
	python3 scripts/literature_search.py
