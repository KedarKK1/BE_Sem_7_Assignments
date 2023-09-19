pragma solidity ^0.8.4;

import "./Token.sol";

contract Bank{
    mapping(address => uint256) public accounts;

    constructor(){

    }

    // external - public to external contracts
    // view - means doent change state of contract
    function totalAssets() view external returns(uint256) {
        return address(this).balance;
    }

    // payable meas we can send value to it
    function deposit() payable external{
        require(msg.value > 0, "Must Deposit more than 0 MATIC!");
        accounts[msg.sender] += msg.value;
    }

    function withdraw(uint256 _amount1, address _tokenContract1) external{
        require(_amount1 <= accounts[msg.sender], "Cannot withdraw more than deposited");

        accounts[msg.sender] -= _amount1;
        payable(msg.sender).transfer(_amount1); // this will transfer matic from SM to user's account

        Token yieldToken = Token(_tokenContract1); // way to make a reference to another SM in solidity 
        yieldToken.mint(msg.sender, 1 ether);

    }

}   