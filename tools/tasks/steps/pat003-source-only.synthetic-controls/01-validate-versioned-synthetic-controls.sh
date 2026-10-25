mkdir -p receipts/pat003
python -m unittest discover -s tests -p 'test_pat003_*_v1.py' -v 2>&1 | tee receipts/pat003/synthetic-controls.log
test "${PIPESTATUS[0]}" -eq 0
