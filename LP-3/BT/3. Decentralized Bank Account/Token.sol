pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol"; // import for using openzeppelin/contracts

contract Token is ERC20 { // for inheritance
    address private bankContract;

    modifier onlyBank() {
        require(msg.sender == bankContract, "Only the bank can mint new Tokens!");
        _; // ! what's this ? - This underscore represents where the modified function's code will be inserted
        // _ in Solidity serves as a placeholder for parameters that are expected but not used within the function or modifier. It's a common convention to make code more readable and to indicate the location where the modified function's code will be inserted in modifiers
    }

    // ERC20("Yields Token", "FREE") is like super of the ERC20 constructor
    constructor(address _bankAddess) ERC20("Yields Token", "FREE"){
        bankContract = _bankAddess;
    }

    function mint(address to1, uint256 amount1) public onlyBank{
        _mint(to1, amount1);
    }
}