# GitHub Actions Workflows

## Sphinx Documentation Deployment

### Overview

The `sphinx-docs.yml` workflow automatically builds and deploys the Sphinx documentation to GitHub Pages whenever changes are pushed to the `main` branch.

### Workflow Triggers

- **Push to main:** Triggers on pushes to `main` branch when documentation files change
- **Pull requests:** Builds documentation for PRs (but doesn't deploy)
- **Manual:** Can be triggered manually via workflow_dispatch

### Files Watched

The workflow triggers when any of these files change:
- `source/**` - Documentation source files
- `requirements.txt` - Python dependencies
- `Makefile` - Build configuration
- `.github/workflows/sphinx-docs.yml` - Workflow itself

### Build Process

1. **Setup:** Checkout code, install Python 3.11, install Graphviz
2. **Dependencies:** Install Python packages from `requirements.txt`
3. **Build:** Run `make html` to build Sphinx documentation
4. **Deploy:** Upload artifact and deploy to GitHub Pages (main branch only)

### GitHub Pages Configuration

To enable GitHub Pages for this repository:

1. Go to **Settings** > **Pages**
2. Set **Source** to "GitHub Actions"
3. The documentation will be available at: `https://[username].github.io/[repo-name]/`

### Local Testing

Before pushing, test the build locally:

```bash
cd sphinx-docs
make html
```

Check for errors in the build output. The built HTML will be in `build/html/`.

### Troubleshooting

**Build fails on GitHub Actions:**
- Check the Actions tab for detailed error logs
- Ensure `requirements.txt` includes all dependencies
- Test the build locally with `make clean && make html`

**Documentation not updating:**
- Check that changes were pushed to the `main` branch
- Verify the workflow completed successfully in the Actions tab
- GitHub Pages can take 2-3 minutes to update after deployment

**Missing dependencies:**
- If sphinx-needs or other extensions fail, update `requirements.txt`
- Re-run the workflow after committing the changes

### Workflow File Location

`.github/workflows/sphinx-docs.yml`
