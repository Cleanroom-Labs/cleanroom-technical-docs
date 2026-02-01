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

.PHONY: help Makefile clean html build-all build-projects copy-projects

# Clean all builds (master and projects)
clean:
	@echo "Cleaning master build..."
	rm -rf $(BUILDDIR)
	@for project in $(PROJECTS); do \
		echo "Cleaning $$project..."; \
		rm -rf $$project/build; \
	done
	@echo "Clean complete"

# Build individual project documentation
build-projects:
	@echo "Building individual project documentation..."
	@for project in $(PROJECTS); do \
		echo ""; \
		echo "Building $$project..."; \
		cd $$project && $(SPHINXBUILD) -M html source build $(SPHINXOPTS) && cd ..; \
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
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
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

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
