#include <iostream>
#include <cassert>
#include <string>

using namespace std;
class Node
{
public:
    Node(int key);
    ~Node();

    Node* left() {return _left;}
    Node* right() {return _right;}
    void left(Node* node) { _left = node;}
    void right(Node* node) { _right = node;}
    int key() {return _key;}
    void key(int key) {_key = key;}

private:
    int _key;
    Node* _left;
    Node* _right;
};

Node::Node(int key) 
: _key(key), 
_left(0), 
_right(0)
{

}

Node::~Node()
{

}

class BinaryTree
{
public:
    BinaryTree();
    ~BinaryTree();

    void insert(int key);
    Node* search(int key);

private:
    /* these are recursive functions to traverse the binary tree */
    void insert(int key, Node* node);
    Node* search(int key, Node* node);
    void destroy(Node* node);

    Node* _root;
};

BinaryTree::BinaryTree()
: _root(0)
{

}

BinaryTree::~BinaryTree()
{
    destroy(_root);
}

void BinaryTree::destroy(Node* node)
{
    if (node == NULL)   return;

    destroy(node->left());
    destroy(node->right());
    delete node;
    node = 0;
}

Node* BinaryTree::search(int key)
{
    return search(key, _root);
}

Node* BinaryTree::search(int key, Node* node)
{
    if (node == NULL)   return NULL;

    int current_value = node->key();
    if (key == current_value)
    {
        return node;
    } 
    
    if (key < current_value)
    {
        search(key, node->left());
    } 
    else
    {
        search(key, node->right());
    }
}

void BinaryTree::insert(int key)
{
    if (_root != NULL)
        insert(key, _root);
    else
        _root = new Node(key);

}

void BinaryTree::insert(int key, Node* node)
{
    if (key < node->key())
    {
        if(node->left())
            insert(key, node->left());
        else
            node->left(new Node(key));
    }
    else if ( key >= node->key())
    {
        if(node->right())
            insert(key, node->right());
        else
            node->right(new Node(key));
    }
}


int main()
{
    // create a binary tree

    // populate the binary tree

    // traverse it

    //assert( atoi("-ksjdhf") == 0);

    cout << "bleh" << endl;
    return 0;
}