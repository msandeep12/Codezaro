# Copilot Linker

A cross-platform Python utility to link agents and skills from the [awesome-copilot](https://github.com/github/awesome-copilot) repository to any local git repository.

## Installation

Install from source:

```bash
pip install .
```

Or for development:

```bash
pip install -e .
```

## Usage

Run the utility from the root of your git repository:

### Link Agents and Skills

```bash
copilot-linker link
```

This will:
- Clone or update the awesome-copilot repository into `.github/awesome-copilot`
- Create symbolic links (or copies if symlinks fail) to `.github/agents` and `.github/skills`
- Add the linked paths to `.gitignore` to prevent them from being committed

### Undo Linking

```bash
copilot-linker undo
```

This will:
- Remove the `.github/agents` and `.github/skills` directories
- Remove the cloned `.github/awesome-copilot` repository

## What it does

- Checks if the current directory is a git repository
- Clones or updates the awesome-copilot repository into `.github/awesome-copilot`
- Creates symbolic links (or copies if symlinks fail):
  - `.github/agents` → `.github/awesome-copilot/agents`
  - `.github/skills` → `.github/awesome-copilot/skills`
- Adds linked paths to `.gitignore`

This allows you to use the agents and skills from awesome-copilot in your repository without copying the files directly.

## Requirements

- Python 3.8+
- Git
- Internet connection for cloning the repository

## Notes

- On systems where symlinks are not supported or require special permissions, the utility will fall back to copying the directories.
- The utility creates links/copies, so changes in the awesome-copilot repo will be reflected in your links (after updating with `git pull` in the cloned directory).
