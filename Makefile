test:
	pytest

tox-test:
	tox

coverage:
	@(coverage run --module pytest $(TEST_OPTIONS) $(TESTS))
