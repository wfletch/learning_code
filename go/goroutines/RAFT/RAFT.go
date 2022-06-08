package main

import (
	"log"
	"sync"
)

type State string

const (
	Follower  = "follower"
	Candidate = "candidate"
	Leader    = "leader"
)

type Raft struct {
	mu          sync.Mutex
	me          int
	peers       []int
	state       State
	currentTerm int
	votedFor    int
}

func (rf *Raft) AttemptElection() {
	rf.mu.Lock()
	rf.state = Candidate
	rf.currentTerm++
	rf.votedFor = rf.me
	log.Printf("[%d] attemping an election at term %d", rf.me, rf.currentTerm)
	rf.mu.Unlock()
}
func main() {

}
