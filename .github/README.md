# GitHub Actions Workflows

## Sphinx Documentation Build & Verification

### Overview

The `sphinx-docs.yml` workflow automatically builds and verifies the Sphinx documentation whenever changes are pushed to the `main` branch. Build artifacts are uploaded for download. Deployment to GitHub Pages is handled separately by the `deploy-tagged.yml` workflow via tagged releases.

### Workflow Triggers

- **Push to main:** Triggers on pushes to `main` branch when documentation files change
- **Pull requests:** Builds documentation for PRs to catch errors early
- **Manual:** Can be triggered manually via workflow_dispatch

### Files Watched

The workflow triggers when any of these files change:
- `source/**` - Documentation source files
- `requirements.txt` - Python dependencies
- `Makefile` - Build configuration
- `.github/workflows/sphinx-docs.yml` - Workflow itself
- `whisper/**`, `deploy/**`, `transfer/**` - Project submodule paths

### Build Process

1. **Setup:** Checkout code with submodules (requires `SUBMODULE_PAT` secret), install Python 3.14, install Graphviz
2. **Verify:** Check all submodules are initialized
3. **Dependencies:** Install Python packages from `requirements.txt`
4. **Build:** Run `make html` to build all project and master documentation
5. **Check:** Run `make html-check` to verify no warnings or errors
6. **Verify:** Ensure project docs are present in build output, check cross-references
7. **Upload:** Upload build artifact

### Prerequisites

1. Configure a `SUBMODULE_PAT` repository secret (GitHub PAT with `repo` scope) for private submodule checkout
2. For deployment via `deploy-tagged.yml`: enable GitHub Pages (Settings > Pages > Source: "GitHub Actions")

### Local Testing

Before pushing, test the build locally:

```bash
cd technical-docs
make html          # Build all documentation
make html-check    # Check for warnings/errors
```

Check for errors in the build output. The built HTML will be in `build/html/`.

### Troubleshooting

**Build fails on GitHub Actions:**
- Check the Actions tab for detailed error logs
- Ensure `SUBMODULE_PAT` secret is configured with `repo` scope
- Test the build locally with `make clean && make html && make html-check`

**Missing dependencies:**
- Dependencies are sourced from `common/requirements.txt` via the shared common submodule
- Re-run the workflow after committing any changes

### Workflow File Location

`.github/workflows/sphinx-docs.yml`
