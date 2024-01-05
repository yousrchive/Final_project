package com.example.basic.model.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import com.example.basic.database.entity.WebEntity;

public interface WebRepository extends JpaRepository<WebEntity, Long> {
    @Query(value = "SELECT a.* FROM account a WHERE a.id = :id", nativeQuery = true)
    WebEntity getUserDtoByUserId(@Param(value = "id") String id);
}
