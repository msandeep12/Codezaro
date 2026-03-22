---
name: "Git MCP Server"
description: "MCP server providing git operations for repository management"
---

# Git MCP Server

This is a Model Context Protocol (MCP) server that provides git operations for the copilot-linker utility.

## Available Tools

### `is_git_repo`
Check if the current directory is a git repository.

**Parameters:**
- None

**Returns:** Boolean indicating if directory is a git repository

### `clone`
Clone a git repository to a target directory.

**Parameters:**
- `repo_url` (string): URL of the repository to clone
- `target_dir` (string): Target directory path

**Returns:** Tuple of (success: boolean, message: string)

### `pull`
Pull updates from a git repository.

**Parameters:**
- `repo_dir` (string): Directory of the repository (default: ".")

**Returns:** Tuple of (success: boolean, message: string)

### `add`
Stage files in git.

**Parameters:**
- `files` (list): List of files to stage
- `repo_dir` (string, optional): Repository directory (default: ".")

**Returns:** Tuple of (success: boolean, message: string)

### `commit`
Commit staged changes.

**Parameters:**
- `message` (string): Commit message
- `repo_dir` (string, optional): Repository directory (default: ".")

**Returns:** Tuple of (success: boolean, message: string)

### `push`
Push changes to remote repository.

**Parameters:**
- `branch` (string, optional): Branch to push (default: "main")
- `repo_dir` (string, optional): Repository directory (default: ".")

**Returns:** Tuple of (success: boolean, message: string)

## Usage in Code

```python
from copilot_linker.git_mcp import GitMCPServer

# Check if in a git repo
if GitMCPServer.is_git_repo():
    print("In a git repository")

# Clone a repository
success, message = GitMCPServer.clone(
    "https://github.com/user/repo.git",
    "./target_dir"
)

# Pull updates
success, message = GitMCPServer.pull("./repo_dir")

# Stage files
success, message = GitMCPServer.add(["file1.py", "file2.py"])

# Commit changes
success, message = GitMCPServer.commit("fix: update files")

# Push to remote
success, message = GitMCPServer.push("main")
```
