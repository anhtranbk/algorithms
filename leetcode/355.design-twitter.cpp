/*
 * @lc app=leetcode id=355 lang=cpp
 *
 * [355] Design Twitter
 */
#include <iostream>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <iterator>
#include <vector>

using namespace std;

// @lc code=start
class Tweet {
public:
    Tweet(int tweetId, int time) : tweetId(tweetId), time(time), next(nullptr) {}

    ~Tweet() {
        delete this->next;
    }

    int tweetId;
    int time;
    Tweet *next;
};

bool operator<(const Tweet &tw1, const Tweet &tw2) {
    return tw1.time < tw2.time;
}

bool operator>(const Tweet &tw1, const Tweet &tw2) {
    return tw1.time > tw2.time;
}

class User {
public:
    User() : tweet_head(nullptr) {}

    ~User() {
        delete tweet_head;
    }

    void postTweet(int tweetId, int time) {
        const auto& tweet = new Tweet(tweetId, time);
        tweet->next = tweet_head;
        tweet_head = tweet;
    }

    void follow(int followeeId) {
        follows.insert(followeeId);
    }

    void unfollow(int followeeId) {
        follows.erase(followeeId);
    }

    Tweet *tweets() const {
        return this->tweet_head;
    }

    Tweet *tweet_head;
    unordered_set<int> follows;
};

class Twitter {
public:
    Twitter() : time(0) {}

    ~Twitter() {
        for (auto &user: users) {
            delete user.second;
        }
    }

    void postTweet(int userId, int tweetId) {
        if (users.find(userId) == users.end()) {
            users[userId] = new(User);
        }
        users[userId]->postTweet(tweetId, this->time++);
    }

    vector<int> getNewsFeed(int userId) {
        vector<int> ans;
        const auto &u = users[userId];
        if (!u) {
            return ans;
        }

        priority_queue<Tweet *> tweets;
        if (u->tweets()) {
            tweets.push(u->tweets());
        }

        for (int followeeId: u->follows) {
            // Approach 1
            if (users.find(followeeId) == users.end()) continue;
            const auto &tw = users[followeeId]->tweets();
            if (tw) {
                tweets.push(tw);
            }

            // Approach 2 (safer)
            // const auto &v = users[followeeId];
            // if (v && v->tweets()) {
            //     tweets.push(v->tweets());
            // }

            // Approach 3
            //
        }

        auto cnt = 10;
        while (cnt-- > 0 && !tweets.empty()) {
            auto tw = tweets.top();
            tweets.pop();

            ans.push_back(tw->tweetId);
            if (tw->next) {
                tweets.push(tw->next);
            }
        }

        return ans;
    }

    void follow(int followerId, int followeeId) {
        if (users.find(followerId) == users.end()) {
            users[followerId] = new(User);
        }
        users[followerId]->follow(followeeId);
    }

    void unfollow(int followerId, int followeeId) {
        if (users.find(followerId) != users.end()) {
            users[followerId]->unfollow(followeeId);
        }
    }

private:
    unordered_map<int, User *> users;
    int time;
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */
// @lc code=end
void printVector(const vector<int> &v) {
    for (const auto &e: v) {
        cout << e << ' ';
    }
    cout << endl;
}

#pragma clang diagnostic push
#pragma ide diagnostic ignored "UnusedParameter"

int main(int argc, char *argv[]) {
    Twitter twitter;

    twitter.postTweet(1, 5);
    printVector(twitter.getNewsFeed(1));

    twitter.postTweet(2, 6);
    twitter.follow(1, 2);
    printVector(twitter.getNewsFeed(1));

    twitter.unfollow(1, 2);
    printVector(twitter.getNewsFeed(1));
}

#pragma clang diagnostic pop