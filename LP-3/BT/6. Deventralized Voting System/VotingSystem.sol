// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract VotingSystem {
    struct Candidate {
        string name;
        uint256 voteCount;
    }

    Candidate[] public candidates;
    mapping(address => bool) public voters;
    address public admin; // Add an admin address


    // constructor(string[] memory _candidateNames) {
    //     for (uint256 i = 0; i < _candidateNames.length; i++) {
    //         candidates.push(Candidate({name: _candidateNames[i], voteCount: 0}));
    //     }
    // }

    constructor(string[] memory _candidateNames) {
        admin = msg.sender; // Set the contract creator as the admin
        for (uint256 i = 0; i < _candidateNames.length; i++) {
            candidates.push(Candidate({name: _candidateNames[i], voteCount: 0}));
        }
    }

    modifier onlyAdmin() {
        require(msg.sender == admin, "Only the admin can call this function.");
        _;
    }

    // Add a new candidate
    function addCandidate(string memory _name) public onlyAdmin {
        candidates.push(Candidate({name: _name, voteCount: 0}));
    }

    function vote(uint256 _candidateIndex) public {
        require(!voters[msg.sender], "You have already voted.");
        require(_candidateIndex < candidates.length, "Invalid candidate index.");

        candidates[_candidateIndex].voteCount++;
        voters[msg.sender] = true;
    }

    function getCandidateCount() public view returns (uint256) {
        return candidates.length;
    }

    function getCandidate(uint256 _index) public view returns (string memory, uint256) {
        require(_index < candidates.length, "Invalid candidate index.");
        Candidate memory candidate = candidates[_index];
        return (candidate.name, candidate.voteCount);
    }
}
