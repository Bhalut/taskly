# Contributing to Taskly

Thank you for considering contributing to Taskly! 🎉  
We welcome community contributions to improve our codebase, features, documentation, and tests.


## 🚀 Development Workflow

1. Fork the repository.
2. Clone your fork locally.
3. Create a new branch from `develop`:
   ```bash
   git checkout develop
   git checkout -b feature/my-new-feature
   ```
4. Make your changes.
5. Run pre-commit checks locally:
   ```bash
   make lint SERVICE=your_service_name
   ```
6. Commit your changes with a meaningful commit message.
7. Push your branch:
   ```bash
   git push origin feature/my-new-feature
   ```
8. Open a Pull Request to merge into `develop`.


## 📦 Branch Naming Convention

| Branch Type | Naming |
|:---|:---|
| Feature | `feature/feature-name` |
| Bugfix | `bugfix/bug-description` |
| Hotfix | `hotfix/critical-fix` |


## 📋 Pull Request Requirements

- PR must be small and focused (preferably < 500 LOC).
- Pass all tests (unit + integration).
- Pass linting and formatting checks.
- Add or update documentation if necessary.
- Provide a clear title and description for the PR.
- Include a reference to the related issue if applicable.

Example:

> "Add user login endpoint #42"


## 🧪 Tests and Quality

- **Unit Tests** must cover new functionality.
- **Integration Tests** must cover API endpoints if applicable.
- Use **pytest** for Python services.
- **Pre-commit hooks** must pass (formatting and linting).

Run tests locally:

```bash
make test SERVICE=your_service_name
```


## 🔥 Release Flow

- All changes go into `develop`.
- After approval, changes can be promoted manually to `staging`.
- To deploy to `production`, a GitHub Release must be created:
  - Tag format: `vX.Y.Z` (example: `v1.0.0`)
  - Include release notes summarizing the changes.


## 💬 Communication

If you have questions, feel free to open a discussion, an issue, or reach out to maintainers. Collaboration and feedback are highly encouraged!


Thank you for your contribution to making Taskly better! 🚀
