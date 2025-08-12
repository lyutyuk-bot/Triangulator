Makefile .PHONY: run test

run:
	cd src && python3 -m triangulator.cli ../data/example_case.json

test:
	pytest -q

## Quick Commands

If you have [Make](https://www.gnu.org/software/make/) installed (macOS includes it by default), you can run the prototype and tests with:

```bash
make run   # Run the prototype with the example dataset
make test  # Run all Python tests in tests/

---

**To add it now:**  
1. Open `README.md` in VS Code.  
2. Scroll to the bottom.  
3. Paste the block above.  
4. Save (**⌘+S**).  
5. Commit and push:
```bash
git add README.md
git commit -m "docs: add Quick Commands section"
git push

# src

Future code for Triangulation Engine, Bias Layer, and Visualization.
