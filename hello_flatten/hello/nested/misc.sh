#!/bin/bash
set -euo pipefail

# Robust hello world with error handling and color output
main() {
    # ANSI color codes for prettier output
    local GREEN='\033[0;32m'
    local NC='\033[0m' # No Color

    echo -e "${GREEN}Hello, World!${NC}"
}

# Execute main function if script is run directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
