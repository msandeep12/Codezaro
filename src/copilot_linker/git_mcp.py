#!/usr/bin/env python3
"""
Git MCP - Git operations via Model Context Protocol
"""

import subprocess
from pathlib import Path
from typing import Tuple


class GitMCPServer:
    """Simple Git MCP Server for git operations."""

    @staticmethod
    def is_git_repo() -> bool:
        """Check if current directory is a git repository."""
        try:
            subprocess.run(
                ["git", "rev-parse", "--git-dir"],
                check=True,
                capture_output=True,
                text=True
            )
            return True
        except subprocess.CalledProcessError:
            return False

    @staticmethod
    def clone(repo_url: str, target_dir: str) -> Tuple[bool, str]:
        """Clone a git repository.
        
        Args:
            repo_url: URL of the repository to clone
            target_dir: Target directory for cloning
            
        Returns:
            Tuple of (success, message)
        """
        try:
            subprocess.run(
                ["git", "clone", repo_url, target_dir],
                check=True,
                capture_output=True,
                text=True
            )
            return True, f"Cloned {repo_url} to {target_dir}"
        except subprocess.CalledProcessError as e:
            return False, f"Clone failed: {e.stderr}"

    @staticmethod
    def pull(repo_dir: str) -> Tuple[bool, str]:
        """Pull updates from a git repository.
        
        Args:
            repo_dir: Directory of the repository
            
        Returns:
            Tuple of (success, message)
        """
        try:
            result = subprocess.run(
                ["git", "-C", repo_dir, "pull"],
                check=True,
                capture_output=True,
                text=True
            )
            return True, f"Updated repository: {result.stdout}"
        except subprocess.CalledProcessError as e:
            return False, f"Pull failed: {e.stderr}"

    @staticmethod
    def add(files: list, repo_dir: str = ".") -> Tuple[bool, str]:
        """Stage files in git.
        
        Args:
            files: List of files to stage
            repo_dir: Directory of the repository
            
        Returns:
            Tuple of (success, message)
        """
        try:
            cmd = ["git", "-C", repo_dir, "add"] + files
            subprocess.run(cmd, check=True, capture_output=True, text=True)
            return True, f"Staged {len(files)} file(s)"
        except subprocess.CalledProcessError as e:
            return False, f"Add failed: {e.stderr}"

    @staticmethod
    def commit(message: str, repo_dir: str = ".") -> Tuple[bool, str]:
        """Commit changes to git.
        
        Args:
            message: Commit message
            repo_dir: Directory of the repository
            
        Returns:
            Tuple of (success, message)
        """
        try:
            result = subprocess.run(
                ["git", "-C", repo_dir, "commit", "-m", message],
                check=True,
                capture_output=True,
                text=True
            )
            return True, f"Committed: {result.stdout}"
        except subprocess.CalledProcessError as e:
            return False, f"Commit failed: {e.stderr}"

    @staticmethod
    def push(branch: str = "main", repo_dir: str = ".") -> Tuple[bool, str]:
        """Push changes to remote repository.
        
        Args:
            branch: Branch to push
            repo_dir: Directory of the repository
            
        Returns:
            Tuple of (success, message)
        """
        try:
            result = subprocess.run(
                ["git", "-C", repo_dir, "push", "origin", branch],
                check=True,
                capture_output=True,
                text=True
            )
            return True, f"Pushed: {result.stdout}"
        except subprocess.CalledProcessError as e:
            return False, f"Push failed: {e.stderr}"
