# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Project submodules
PROJECTS = whisper deploy transfer

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile clean html build-all build-projects copy-projects html-check

# Clean all builds (master and projects)
clean:
	@echo "Cleaning master build..."
	rm -rf $(BUILDDIR)
	rm -f build.log
	@for project in $(PROJECTS); do \
		echo "Cleaning $$project..."; \
		rm -rf $$project/build; \
	done
	@echo "Clean complete"

# Build individual project documentation
build-projects:
	@echo "Building individual project documentation..."
	@rm -f build.log
	@for project in $(PROJECTS); do \
		echo ""; \
		echo "Building $$project..."; \
		cd $$project && $(SPHINXBUILD) -M html source build $(SPHINXOPTS) 2>&1 | tee -a ../build.log && cd ..; \
	done
	@echo ""
	@echo "✓ All project documentation built"

# Copy project docs into master build
copy-projects:
	@echo "Copying project documentation into master build..."
	@mkdir -p $(BUILDDIR)/html
	@for project in $(PROJECTS); do \
		project_name=$$project; \
		echo "  Copying $$project_name..."; \
		mkdir -p $(BUILDDIR)/html/$$project_name; \
		cp -r $$project/build/html/* $(BUILDDIR)/html/$$project_name/; \
	done
	@echo "✓ Project documentation copied"

# Build everything (projects + master + copy)
html: build-projects
	@echo ""
	@echo "Building master documentation..."
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) 2>&1 | tee -a build.log
	@$(MAKE) copy-projects
	@echo ""
	@echo "✓ Complete build finished"
	@echo "  Master docs: $(BUILDDIR)/html/index.html"
	@echo "  Project docs copied to:"
	@for project in $(PROJECTS); do \
		project_name=$$project; \
		echo "    - $(BUILDDIR)/html/$$project_name/"; \
	done

# Alias for html
build-all: html

# Fallback rule: trigger a build if build.log doesn't exist
build.log:
	@$(MAKE) html

# Check build log for warnings (run after 'make html')
html-check: build.log
	@ERRORS="$$(grep -E 'ERROR:' build.log || true)"; \
	WARNINGS="$$(grep -E 'WARNING:' build.log || true)"; \
	NON_IGNORED="$$(echo "$$WARNINGS" | grep -viE 'failed to reach any of the inventories|intersphinx inventory' || true)"; \
	if [ -n "$$ERRORS" ]; then \
		echo ""; \
		echo "❌ Build completed with errors:"; \
		echo "$$ERRORS"; \
		exit 1; \
	fi; \
	if [ -n "$$NON_IGNORED" ]; then \
		echo ""; \
		echo "❌ Build completed with warnings:"; \
		echo "$$NON_IGNORED"; \
		exit 1; \
	fi; \
	if [ -n "$$WARNINGS" ]; then \
		IGNORED_COUNT="$$(echo "$$WARNINGS" | wc -l | tr -d ' ')"; \
		echo "✓ No warnings found ($$IGNORED_COUNT intersphinx inventory warning(s) ignored)"; \
	else \
		echo "✓ No warnings found"; \
	fi

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
