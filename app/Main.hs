{-# LANGUAGE OverloadedStrings #-}
module Main where

import           Network.Beanstalk


-- A Beanstalk producer
main :: IO ()
main = do
  client <- connectBeanstalk "127.0.0.1" "11300"
  job <- putJob client 1111 0 300 "Haskell hello"
  disconnectBeanstalk client
