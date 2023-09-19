// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    // Define a structure to represent a student
    struct Student {
        uint256 id;
        string name;
        uint256 age;
    }

    // Create an array to store student data
    Student[] public students;

    // Create a mapping to store Ether received and sender addresses
    mapping(address => uint256) public etherReceived;


    // Add a new student to the array
    function addStudent(uint256 _id, string memory _name, uint256 _age) public {
        students.push(Student(_id, _name, _age));
    }

    // Get the total number of students
    function getStudentCount() public view returns (uint256) {
        return students.length;
    }

    // Get student data by index
    function getStudent(uint256 index) public view returns (uint256, string memory, uint256) {
        require(index < students.length, "Invalid index");
        Student memory student = students[index];
        return (student.id, student.name, student.age);
    }

    // Fallback function to receive Ether
    receive() external payable {
        // Store the sender's address and the amount of Ether received
        address sender = msg.sender;
        uint256 amount = msg.value;
        
        etherReceived[sender] += amount;
        // You can add more custom logic here, such as emitting an event or updating state variables.
    }

}
